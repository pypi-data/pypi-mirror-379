"""Atlassian MCP Server with seamless OAuth 2.0 flow for Jira and Confluence."""

import asyncio
import base64
import functools
import hashlib
import json
import logging
import os
import secrets
import sys
import threading
import time
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import parse_qs, urlencode, urlparse

# Configure logging to both stderr and file
log_file = Path.home() / ".atlassian-mcp-debug.log"
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler(log_file)
    ]
)
logger = logging.getLogger(__name__)

import httpx
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel


class AtlassianConfig(BaseModel):
    """Configuration for Atlassian Cloud connection."""
    site_url: str
    client_id: str
    client_secret: str
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None


class AtlassianError(Exception):
    """Structured error for AI agent consumption."""
    def __init__(self, message: str, error_code: str, context: Dict[str, Any] = None, 
                 troubleshooting: List[str] = None, suggested_actions: List[str] = None):
        super().__init__(message)
        self.error_code = error_code
        self.context = context or {}
        self.troubleshooting = troubleshooting or []
        self.suggested_actions = suggested_actions or []
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": False,
            "error": str(self),
            "error_code": self.error_code,
            "context": self.context,
            "troubleshooting": self.troubleshooting,
            "suggested_actions": self.suggested_actions
        }


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handle OAuth callback automatically."""
    
    def do_GET(self):
        if self.path.startswith('/callback'):
            parsed = urlparse(self.path)
            query_params = parse_qs(parsed.query)
            
            self.server.callback_data = {
                'code': query_params.get('code', [None])[0],
                'state': query_params.get('state', [None])[0],
                'error': query_params.get('error', [None])[0]
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            if self.server.callback_data['error']:
                html = f"""<html>
<head><title>Authorization Failed</title></head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
    <h1 style="color: #d73527;">Authorization Failed</h1>
    <p>Error: {self.server.callback_data['error']}</p>
</body></html>"""
            else:
                html = """<html>
<head><title>Authorization Successful</title></head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
    <h1 style="color: #36b37e;">Authorization Successful!</h1>
    <p>You can close this window.</p>
    <script>setTimeout(() => window.close(), 3000);</script>
</body></html>"""
            
            self.wfile.write(html.encode('utf-8'))
            self.server.callback_received = True
        else:
            self.send_error(404)
    
    def log_message(self, format, *args):
        pass


class AtlassianClient:
    """HTTP client for Atlassian Cloud APIs with seamless OAuth 2.0 flow."""
    
    def __init__(self, config: AtlassianConfig):
        self.config = config
        self.client = httpx.AsyncClient()
        self.credentials_file = Path.home() / ".atlassian_mcp_credentials.json"
        self.server = None
        self.server_thread = None
    
    def generate_pkce(self):
        """Generate PKCE codes"""
        code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8').rstrip('=')
        code_challenge = base64.urlsafe_b64encode(
            hashlib.sha256(code_verifier.encode('utf-8')).digest()
        ).decode('utf-8').rstrip('=')
        return code_verifier, code_challenge
    
    def start_callback_server(self):
        """Start the callback server"""
        self.server = HTTPServer(('localhost', 8080), OAuthCallbackHandler)
        self.server.callback_received = False
        self.server.callback_data = None
        
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
    
    def stop_callback_server(self):
        """Stop the callback server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            if self.server_thread:
                self.server_thread.join(timeout=1)
    
    async def seamless_oauth_flow(self):
        """Complete OAuth flow with automatic callback handling"""
        # Start callback server
        self.start_callback_server()
        
        try:
            # Generate PKCE
            code_verifier, code_challenge = self.generate_pkce()
            state = secrets.token_urlsafe(32)
            
            # Minimal required scopes for MCP functionality
            scopes = [
                # Jira - Essential for ticket operations
                "read:jira-work",                    # Read issues, projects
                "read:jira-user",                    # Read user info
                "write:jira-work",                   # Create/update issues
                
                # Confluence - Enhanced scopes for full functionality
                "read:page:confluence",              # Read pages (replaces read:confluence-content.all)
                "read:space:confluence",             # Read space info (replaces read:confluence-space.summary)
                "write:page:confluence",             # Create/update pages (replaces write:confluence-content)
                "read:comment:confluence",           # Read comments
                "write:comment:confluence",          # Create comments
                "read:label:confluence",             # Read labels
                "read:attachment:confluence",        # Read attachments
                
                # Service Management - Classic scopes (not granular)
                "read:servicedesk-request",          # Read service desk requests
                "write:servicedesk-request",         # Create/update service desk requests
                "manage:servicedesk-customer",       # Manage service desk customers and participants
                
                # Core
                "read:me",                           # User profile
                "offline_access"                     # Token refresh
            ]
            
            params = {
                "audience": "api.atlassian.com",
                "client_id": self.config.client_id,
                "scope": " ".join(scopes),
                "redirect_uri": "http://localhost:8080/callback",
                "state": state,
                "response_type": "code",
                "prompt": "consent"
            }
            
            auth_url = f"https://auth.atlassian.com/authorize?{urlencode(params)}"
            
            print("🚀 Starting Atlassian OAuth authentication...")
            print("🌐 Opening browser for authorization...")
            webbrowser.open(auth_url)
            
            # Wait for callback
            timeout = 300  # 5 minutes
            start_time = time.time()
            
            while not self.server.callback_received:
                if time.time() - start_time > timeout:
                    raise TimeoutError("Authorization timed out after 5 minutes")
                await asyncio.sleep(0.5)
            
            callback_data = self.server.callback_data
            
            if callback_data['error']:
                raise ValueError(f"OAuth error: {callback_data['error']}")
            
            if callback_data['state'] != state:
                raise ValueError("Invalid state parameter")
            
            print("✅ Authorization received, exchanging for tokens...")
            
            # Exchange code for tokens
            token_data = {
                "grant_type": "authorization_code",
                "client_id": self.config.client_id,
                "client_secret": self.config.client_secret,
                "code": callback_data['code'],
                "redirect_uri": "http://localhost:8080/callback"
            }
            
            response = await self.client.post(
                "https://auth.atlassian.com/oauth/token",
                data=token_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            
            if response.status_code != 200:
                raise ValueError(f"Token exchange failed: {response.text}")
            
            tokens = response.json()
            
            # Save tokens
            self.config.access_token = tokens["access_token"]
            self.config.refresh_token = tokens.get("refresh_token")
            self.save_credentials()
            
            print("✅ OAuth flow completed successfully!")
            return tokens
                
        finally:
            self.stop_callback_server()
    
    def save_credentials(self):
        """Save credentials to file"""
        credentials = {
            "access_token": self.config.access_token,
            "refresh_token": self.config.refresh_token,
            "site_url": self.config.site_url,
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret
        }
        
        with open(self.credentials_file, 'w') as f:
            json.dump(credentials, f, indent=2)
        self.credentials_file.chmod(0o600)
    
    def load_credentials(self) -> bool:
        """Load saved credentials"""
        if not self.credentials_file.exists():
            return False
        
        try:
            with open(self.credentials_file, 'r') as f:
                creds = json.load(f)
            
            self.config.access_token = creds.get("access_token")
            self.config.refresh_token = creds.get("refresh_token")
            return bool(self.config.access_token)
        except Exception:
            return False
    
    async def refresh_access_token(self) -> bool:
        """Refresh access token using refresh token"""
        if not self.config.refresh_token:
            return False
        
        token_data = {
            "grant_type": "refresh_token",
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "refresh_token": self.config.refresh_token
        }
        
        try:
            response = await self.client.post(
                "https://auth.atlassian.com/oauth/token",
                data=token_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            response.raise_for_status()
            
            tokens = response.json()
            self.config.access_token = tokens["access_token"]
            self.save_credentials()
            return True
        except Exception:
            return False
    
    async def get_headers(self) -> Dict[str, str]:
        """Get authenticated headers"""
        if not self.config.access_token:
            raise ValueError("No access token available. Please authenticate first.")
        
        return {
            "Authorization": f"Bearer {self.config.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    
    async def make_request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Make authenticated request with enhanced error handling and debugging."""
        # Extract operation context for debugging
        operation_context = kwargs.pop('operation_context', {})
        operation_name = operation_context.get('name', 'unknown')
        
        logger.debug(f"make_request: {method} {url} - Operation: {operation_name}")
        
        try:
            headers = await self.get_headers()
            kwargs.setdefault('headers', {}).update(headers)
            
            response = await self.client.request(method, url, **kwargs)
            
            # Try to refresh token if unauthorized
            if response.status_code == 401 and self.config.refresh_token:
                logger.debug(f"make_request: Token expired, refreshing for operation: {operation_name}")
                if await self.refresh_access_token():
                    headers = await self.get_headers()
                    kwargs['headers'].update(headers)
                    response = await self.client.request(method, url, **kwargs)
            
            # Enhanced error handling with structured responses
            if response.status_code == 401:
                raise AtlassianError(
                    "Authentication required - access token expired or invalid",
                    "AUTH_REQUIRED",
                    context={"operation": operation_name, "url": url},
                    troubleshooting=["Access token may have expired", "OAuth scopes may be insufficient"],
                    suggested_actions=["authenticate_atlassian()"]
                )
            
            # Service Management specific errors
            if response.status_code == 404 and '/servicedeskapi/' in url:
                if '/request/' in url:
                    raise AtlassianError(
                        "Service desk request not found",
                        "SERVICEDESK_REQUEST_NOT_FOUND",
                        context={"operation": operation_name, "url": url},
                        troubleshooting=[
                            "Issue may be a regular Jira issue (not service desk request)",
                            "Missing OAuth scopes for Service Management",
                            "Insufficient permissions for Service Management"
                        ],
                        suggested_actions=["authenticate_atlassian()", "servicedesk_check_availability()"]
                    )
                else:
                    raise AtlassianError(
                        "Service desk endpoint not found",
                        "SERVICEDESK_ENDPOINT_NOT_FOUND", 
                        context={"operation": operation_name, "url": url},
                        troubleshooting=["Missing OAuth scopes for Service Management"],
                        suggested_actions=["authenticate_atlassian()"]
                    )
            
            if response.status_code == 403 and '/servicedeskapi/' in url:
                raise AtlassianError(
                    "Access denied to Service Management",
                    "SERVICEDESK_ACCESS_DENIED",
                    context={"operation": operation_name, "url": url},
                    troubleshooting=[
                        "User may lack Service Management permissions",
                        "OAuth scopes may be insufficient"
                    ],
                    suggested_actions=["authenticate_atlassian()", "Contact Atlassian administrator"]
                )
            
            # Generic HTTP errors
            if not response.is_success:
                logger.error(f"make_request: HTTP {response.status_code} - {response.text} [operation={operation_name}]")
                raise AtlassianError(
                    f"HTTP {response.status_code}: {response.text}",
                    f"HTTP_{response.status_code}",
                    context={"operation": operation_name, "url": url, "status_code": response.status_code},
                    troubleshooting=[f"Server returned {response.status_code} error"],
                    suggested_actions=["Check request parameters", "Verify permissions"]
                )
            
            logger.debug(f"make_request: Success {response.status_code} [operation={operation_name}]")
            return response
            
        except AtlassianError:
            # Re-raise structured errors as-is
            raise
        except Exception as e:
            logger.error(f"make_request: Unexpected error - {e} [operation={operation_name}]")
            raise AtlassianError(
                f"Unexpected error: {e}",
                "UNEXPECTED_ERROR",
                context={"operation": operation_name, "url": url},
                troubleshooting=["Check network connection", "Verify request parameters"],
                suggested_actions=["Retry the operation", "Check logs for details"]
            )
    
    async def get_cloud_id(self, required_scopes: Optional[List[str]] = None) -> str:
        """Get the cloud ID for the configured site, optionally filtering by required scopes"""
        url = "https://api.atlassian.com/oauth/token/accessible-resources"
        response = await self.make_request("GET", url)
        resources = response.json()
        
        matching_resources = []
        for resource in resources:
            if resource["url"] == self.config.site_url:
                matching_resources.append(resource)
        
        if not matching_resources:
            raise ValueError(f"Site {self.config.site_url} not found in accessible resources")
        
        # If specific scopes are required, find resource with those scopes
        if required_scopes:
            for resource in matching_resources:
                resource_scopes = resource.get("scopes", [])
                if all(scope in resource_scopes for scope in required_scopes):
                    return resource["id"]
            raise ValueError(f"No resource found with required scopes: {required_scopes}")
        
        # Default: return first matching resource
        return matching_resources[0]["id"]
    
    # Jira Methods
    async def jira_search(self, jql: str, max_results: int = 50) -> List[Dict[str, Any]]:
        """Search Jira issues using JQL"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/search"
        data = {"jql": jql, "maxResults": max_results, "fields": ["summary", "status", "assignee", "priority", "issuetype", "description"]}
        
        response = await self.make_request("POST", url, json=data)
        return response.json().get("issues", [])
    
    async def jira_get_issue(self, issue_key: str) -> Dict[str, Any]:
        """Get Jira issue details"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/issue/{issue_key}"
        
        response = await self.make_request("GET", url)
        return response.json()
    
    async def jira_create_issue(self, project_key: str, summary: str, description: str, issue_type: str = "Task") -> Dict[str, Any]:
        """Create a new Jira issue"""
        cloud_id = await self.get_cloud_id()
        
        # First get valid issue types for the project
        project_url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/project/{project_key}"
        project_response = await self.make_request("GET", project_url)
        project_data = project_response.json()
        
        # Find the issue type (use first available if specified type not found)
        issue_types = project_data.get('issueTypes', [])
        issue_type_id = None
        
        for it in issue_types:
            if it['name'].lower() == issue_type.lower():
                issue_type_id = it['id']
                break
        
        if not issue_type_id and issue_types:
            issue_type_id = issue_types[0]['id']  # Use first available
        
        if not issue_type_id:
            raise ValueError(f"No valid issue types found for project {project_key}")
        
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/issue"
        data = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": description
                                }
                            ]
                        }
                    ]
                },
                "issuetype": {"id": issue_type_id}
            }
        }
        
        response = await self.make_request("POST", url, json=data)
        return response.json()
    
    async def jira_update_issue(self, issue_key: str, summary: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
        """Update a Jira issue"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/issue/{issue_key}"
        
        fields = {}
        if summary:
            fields["summary"] = summary
        if description:
            fields["description"] = {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                        ]
                    }
                ]
            }
        
        data = {"fields": fields}
        response = await self.make_request("PUT", url, json=data)
        return {"success": True, "issue_key": issue_key}
    
    async def jira_add_comment(self, issue_key: str, comment: str) -> Dict[str, Any]:
        """Add a comment to a Jira issue"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/api/3/issue/{issue_key}/comment"
        
        data = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": comment
                            }
                        ]
                    }
                ]
            }
        }
        
        response = await self.make_request("POST", url, json=data)
        return response.json()
    
    # Confluence Methods
    async def confluence_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search Confluence content using v2 API"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages"
        params = {"title": query, "limit": limit, "body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_get_page(self, page_id: str) -> Dict[str, Any]:
        """Get Confluence page content"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}"
        params = {"body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json()
    
    async def confluence_create_page(self, space_key: str, title: str, content: str, parent_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new Confluence page"""
        try:
            # Use same cloud ID approach as working read operations
            cloud_id = await self.get_cloud_id()
            
            # Debug: Check accessible resources and scopes
            resources_url = "https://api.atlassian.com/oauth/token/accessible-resources"
            resources_response = await self.make_request("GET", resources_url)
            resources_data = resources_response.json()
            
            # Debug info for cloud ID selection
            cloud_id_debug = {
                "requested_scopes": ["write:confluence-content"],
                "available_resources": resources_data,
                "selected_cloud_id": cloud_id
            }
            
            # Get space ID from space key using v2 API
            space_url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/spaces"
            space_response = await self.make_request("GET", space_url, params={"keys": space_key})
            spaces = space_response.json().get("results", [])
            if not spaces:
                return {"error": f"Space '{space_key}' not found"}
            space_id = spaces[0]["id"]
            
            url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages"
            
            data = {
                "spaceId": space_id,
                "status": "current",
                "title": title,
                "body": {
                    "representation": "storage",
                    "value": content
                },
                "subtype": "live"
            }
            
            if parent_id:
                data["parentId"] = parent_id
            
            # Debug the actual API call
            try:
                # Check if we have access token before making request
                headers_debug = await self.get_headers()
                response = await self.make_request("POST", url, json=data)
                return response.json()
            except ValueError as auth_error:
                return {
                    "error": f"Authentication error: {str(auth_error)}",
                    "debug_info": {
                        "cloud_id_selection": cloud_id_debug,
                        "api_url": url,
                        "request_data": data,
                        "space_id": space_id,
                        "access_token_present": bool(self.config.access_token),
                        "access_token_length": len(self.config.access_token) if self.config.access_token else 0,
                        "refresh_token_present": bool(self.config.refresh_token),
                        "site_url": self.config.site_url
                    }
                }
            except Exception as api_error:
                return {
                    "error": f"API call failed: {str(api_error)}",
                    "debug_info": {
                        "cloud_id_selection": cloud_id_debug,
                        "api_url": url,
                        "request_data": data,
                        "space_id": space_id,
                        "headers_used": await self.get_headers() if hasattr(self, 'get_headers') else "Unable to get headers"
                    }
                }
            
        except Exception as e:
            # Return debug info with the error
            return {
                "error": str(e),
                "debug_info": {
                    "site_url": self.config.site_url,
                    "has_access_token": bool(self.config.access_token),
                    "cloud_id_selection": cloud_id_debug if 'cloud_id_debug' in locals() else "Failed before cloud ID selection",
                    "accessible_resources": resources_data if 'resources_data' in locals() else "Failed to retrieve",
                    "cloud_id": cloud_id if 'cloud_id' in locals() else "Failed to retrieve"
                }
            }
    
    async def confluence_update_page(self, page_id: str, title: str, content: str, version: int) -> Dict[str, Any]:
        """Update an existing Confluence page"""
        # Get cloud ID for resource with Confluence write scope
        cloud_id = await self.get_cloud_id(required_scopes=["write:page:confluence"])
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}"
        
        data = {
            "id": page_id,
            "status": "current", 
            "title": title,
            "body": {
                "representation": "storage",
                "value": content
            },
            "version": {
                "number": version + 1
            }
        }
        
        response = await self.make_request("PUT", url, json=data)
        return response.json()
    
    # Phase 1: Space Management
    async def confluence_list_spaces(self, limit: int = 25, space_type: Optional[str] = None, status: str = "current") -> List[Dict[str, Any]]:
        """List Confluence spaces with filtering options."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/spaces"
        
        params = {"limit": limit, "status": status}
        if space_type:
            params["type"] = space_type
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_get_space(self, space_id: str, include_icon: bool = False) -> Dict[str, Any]:
        """Get detailed information about a specific space."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/spaces/{space_id}"
        
        params = {"include-icon": include_icon}
        
        response = await self.make_request("GET", url, params=params)
        return response.json()
    
    async def confluence_get_space_pages(self, space_id: str, limit: int = 25, status: str = "current") -> List[Dict[str, Any]]:
        """Get pages in a specific space."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages"
        
        params = {
            "space-id": space_id,
            "limit": limit,
            "status": status,
            "body-format": "storage"
        }
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    # Phase 2: Enhanced Search & Discovery
    async def confluence_search_content(self, query: str, limit: int = 25, space_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Advanced search across Confluence content."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages"
        
        params = {"title": query, "limit": limit, "body-format": "storage"}
        if space_id:
            params["space-id"] = space_id
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_get_page_children(self, page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """Get child pages of a specific page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}/children"
        
        params = {"limit": limit, "body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    
    # Phase 3: Comments & Collaboration
    async def confluence_get_page_comments(self, page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """Get comments for a specific page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/footer-comments"
        
        params = {
            "page-id": page_id,
            "limit": limit,
            "body-format": "storage"
        }
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_add_comment(self, page_id: str, comment: str, parent_comment_id: Optional[str] = None) -> Dict[str, Any]:
        """Add a comment to a page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/footer-comments"
        
        data = {
            "pageId": page_id,
            "body": {
                "representation": "storage",
                "value": comment
            }
        }
        
        if parent_comment_id:
            data["parentCommentId"] = parent_comment_id
        
        response = await self.make_request("POST", url, json=data)
        return response.json()
    
    async def confluence_get_comment(self, comment_id: str) -> Dict[str, Any]:
        """Get a specific comment by ID."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/footer-comments/{comment_id}"
        
        params = {"body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json()
    
    # Phase 4: Labels & Organization
    async def confluence_get_page_labels(self, page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """Get labels for a specific page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}/labels"
        
        params = {"limit": limit}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_search_by_label(self, label_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """Find pages with a specific label."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/labels/{label_id}/pages"
        
        params = {"limit": limit, "body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_list_labels(self, limit: int = 25, prefix: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all labels with optional filtering."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/labels"
        
        params = {"limit": limit}
        if prefix:
            params["prefix"] = prefix
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    # Phase 5: Attachments
    async def confluence_get_page_attachments(self, page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """Get attachments for a specific page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}/attachments"
        
        params = {"limit": limit}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_get_attachment(self, attachment_id: str) -> Dict[str, Any]:
        """Get details of a specific attachment."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/attachments/{attachment_id}"
        
        response = await self.make_request("GET", url)
        return response.json()
    
    # Phase 6: Version History
    async def confluence_get_page_versions(self, page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """Get version history for a page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}/versions"
        
        params = {"limit": limit, "body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("results", [])
    
    async def confluence_get_page_version(self, page_id: str, version_number: int) -> Dict[str, Any]:
        """Get a specific version of a page."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/confluence/{cloud_id}/wiki/api/v2/pages/{page_id}/versions/{version_number}"
        
        params = {"body-format": "storage"}
        
        response = await self.make_request("GET", url, params=params)
        return response.json()    
    # Service Management Methods
    
    # Phase 2: Critical Missing Tools - Service Desk Discovery
    async def servicedesk_list_service_desks(self, limit: int = 50) -> List[Dict[str, Any]]:
        """List available service desks for creating requests.
        
        Essential for AI agents to discover service desks before creating requests.
        This is typically the first tool to call when working with Service Management.
        
        Args:
            limit: Maximum number of service desks to return (default: 50, max: 100)
        
        Returns:
            List of service desk objects with id, projectId, projectName, and projectKey
            
        Example:
            # Get all available service desks
            service_desks = await servicedesk_list_service_desks()
            
            # Use first service desk for request creation
            if service_desks:
                service_desk_id = service_desks[0]["id"]
        
        Common Errors:
            - "Access denied": User may lack Service Management permissions
            - "Endpoint not found": Missing OAuth scopes - re-authenticate
        """
        logger.debug(f"servicedesk_list_service_desks: Fetching service desks (limit={limit})")
        
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/servicedesk"
        params = {"limit": limit}
        
        response = await self.make_request(
            "GET", url, params=params,
            operation_context={"name": "servicedesk_list_service_desks", "limit": limit}
        )
        
        results = response.json().get("values", [])
        logger.debug(f"servicedesk_list_service_desks: Found {len(results)} service desks")
        return results
    
    async def servicedesk_get_service_desk(self, service_desk_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific service desk.
        
        Args:
            service_desk_id: Service desk identifier
        
        Returns:
            Service desk object with detailed information
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/servicedesk/{service_desk_id}"
        
        response = await self.make_request("GET", url)
        return response.json()
    
    # Phase 2: Critical Missing Tools - Request Type Discovery
    async def servicedesk_list_request_types(self, service_desk_id: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
        """List available request types for creating service desk requests.
        
        Essential for AI agents to discover request types before creating requests.
        
        Args:
            service_desk_id: Optional service desk ID to filter request types.
                           If None, returns request types from all accessible service desks.
            limit: Maximum number of request types to return (default: 50, max: 100)
        
        Returns:
            List of request type objects with id, name, description, and serviceDeskId
        """
        cloud_id = await self.get_cloud_id()
        
        if service_desk_id:
            url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/servicedesk/{service_desk_id}/requesttype"
        else:
            url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/requesttype"
        
        params = {"limit": limit}
        response = await self.make_request("GET", url, params=params)
        return response.json().get("values", [])
    
    async def servicedesk_get_request_type(self, service_desk_id: str, request_type_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific request type.
        
        Args:
            service_desk_id: Service desk identifier
            request_type_id: Request type identifier
        
        Returns:
            Request type object with detailed information
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/servicedesk/{service_desk_id}/requesttype/{request_type_id}"
        
        response = await self.make_request("GET", url)
        return response.json()
    
    async def servicedesk_get_request_type_fields(self, service_desk_id: str, request_type_id: str) -> List[Dict[str, Any]]:
        """Get required and optional fields for a specific request type.
        
        Essential for understanding what fields are needed when creating requests.
        
        Args:
            service_desk_id: Service desk identifier
            request_type_id: Request type identifier
        
        Returns:
            List of field objects with fieldId, name, required, and other metadata
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/servicedesk/{service_desk_id}/requesttype/{request_type_id}/field"
        
        response = await self.make_request("GET", url)
        return response.json().get("requestTypeFields", [])
    
    # Phase 2: Enhanced Request Management
    async def servicedesk_get_request_comments(self, issue_key: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get comments for a service desk request.
        
        Args:
            issue_key: Service desk request key
            limit: Maximum number of comments to return (default: 50)
        
        Returns:
            List of comment objects with body, author, created date, and visibility
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/comment"
        params = {"limit": limit}
        
        response = await self.make_request("GET", url, params=params)
        return response.json().get("values", [])
    
    async def servicedesk_get_request_transitions(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get available transitions for a service desk request.
        
        Args:
            issue_key: Service desk request key
        
        Returns:
            List of transition objects with id, name, and to status
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/transition"
        
        response = await self.make_request("GET", url)
        return response.json().get("values", [])
    
    async def servicedesk_transition_request(self, issue_key: str, transition_id: str, comment: Optional[str] = None) -> Dict[str, Any]:
        """Transition a service desk request to a new status.
        
        Args:
            issue_key: Service desk request key
            transition_id: ID of the transition to perform
            comment: Optional comment to add with the transition
        
        Returns:
            Success confirmation with transition details
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/transition"
        
        data = {"id": transition_id}
        if comment:
            data["additionalComment"] = {"body": comment}
        
        response = await self.make_request("POST", url, json=data)
        return response.json()

    async def servicedesk_get_requests(self, service_desk_id: Optional[str] = None, limit: int = 50, start: int = 0) -> List[Dict[str, Any]]:
        """Get service desk requests with enhanced pagination."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request"
        
        params = {"limit": limit, "start": start}
        if service_desk_id:
            params["serviceDeskId"] = service_desk_id
            
        response = await self.make_request(
            "GET", url, params=params,
            operation_context={"name": "servicedesk_get_requests", "service_desk_id": service_desk_id, "limit": limit, "start": start}
        )
        return response.json().get("values", [])
    
    async def servicedesk_get_request(self, issue_key: str) -> Dict[str, Any]:
        """Get specific service desk request details"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}"
        
        response = await self.make_request("GET", url)
        return response.json()
    
    async def servicedesk_create_request(self, service_desk_id: str, request_type_id: str, summary: str, description: str) -> Dict[str, Any]:
        """Create a new service desk request"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request"
        
        data = {
            "serviceDeskId": service_desk_id,
            "requestTypeId": request_type_id,
            "requestFieldValues": {
                "summary": summary,
                "description": description
            }
        }
        
        response = await self.make_request(
            "POST", url, json=data,
            operation_context={"name": "servicedesk_create_request", "service_desk_id": service_desk_id, "request_type_id": request_type_id}
        )
        return response.json()
    
    async def servicedesk_add_comment(self, issue_key: str, comment: str, public: bool = True) -> Dict[str, Any]:
        """Add comment to service desk request"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/comment"
        
        data = {
            "body": comment,
            "public": public
        }
        
        response = await self.make_request("POST", url, json=data)
        return response.json()
    
    async def servicedesk_get_request_status(self, issue_key: str) -> Dict[str, Any]:
        """Get service desk request status"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/status"
        
        response = await self.make_request("GET", url)
        return response.json()
    
    # Phase 2: Approval workflows and participant management
    async def servicedesk_get_approvals(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get approval information for a service desk request"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/approval"
        
        response = await self.make_request("GET", url)
        return response.json().get("values", [])
    
    async def servicedesk_approve_request(self, issue_key: str, approval_id: str, decision: str) -> Dict[str, Any]:
        """Approve or decline a service desk request approval
        
        Args:
            issue_key: The service desk request key
            approval_id: The approval ID to respond to
            decision: 'approve' or 'decline'
        """
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/approval/{approval_id}"
        
        data = {"decision": decision}
        response = await self.make_request("POST", url, json=data)
        return response.json()
    
    async def servicedesk_get_participants(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get participants for a service desk request"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/participant"
        
        response = await self.make_request("GET", url)
        return response.json().get("values", [])
    
    async def servicedesk_add_participants(self, issue_key: str, usernames: List[str]) -> Dict[str, Any]:
        """Add participants to a service desk request"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/participant"
        
        data = {"usernames": usernames}
        response = await self.make_request("POST", url, json=data)
        return response.json()
    
    async def servicedesk_manage_notifications(self, issue_key: str, subscribe: bool) -> Dict[str, Any]:
        """Subscribe or unsubscribe from service desk request notifications"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/notification"
        
        if subscribe:
            response = await self.make_request("PUT", url)
        else:
            response = await self.make_request("DELETE", url)
        
        return {"success": True, "subscribed": subscribe}
    
    # Phase 3: Advanced Features - SLA & Performance Tracking
    async def servicedesk_get_request_sla(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get SLA information for a service desk request."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/sla"
        
        response = await self.make_request(
            "GET", url,
            operation_context={"name": "servicedesk_get_request_sla", "issue_key": issue_key}
        )
        return response.json().get("values", [])
    
    async def servicedesk_get_sla_metric(self, issue_key: str, sla_metric_id: str) -> Dict[str, Any]:
        """Get detailed SLA metric information."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/sla/{sla_metric_id}"
        
        response = await self.make_request(
            "GET", url,
            operation_context={"name": "servicedesk_get_sla_metric", "issue_key": issue_key, "sla_metric_id": sla_metric_id}
        )
        return response.json()

    # Phase 3: Advanced Features - Attachment Management  
    async def servicedesk_get_request_attachments(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get attachments for a service desk request."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/request/{issue_key}/attachment"
        
        response = await self.make_request(
            "GET", url,
            operation_context={"name": "servicedesk_get_request_attachments", "issue_key": issue_key}
        )
        return response.json().get("values", [])

    # Phase 3: Advanced Features - Knowledge Base Integration
    async def servicedesk_search_knowledge_base(self, query: str, service_desk_id: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search knowledge base articles."""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/knowledgebase/article"
        
        params = {"query": query, "limit": limit}
        if service_desk_id:
            params["serviceDeskId"] = service_desk_id
        
        response = await self.make_request(
            "GET", url, params=params,
            operation_context={"name": "servicedesk_search_knowledge_base", "query": query, "service_desk_id": service_desk_id}
        )
        return response.json().get("values", [])
    
    async def servicedesk_debug_request(self, endpoint: str) -> Dict[str, Any]:
        """Debug Service Management API requests to see actual responses"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/{endpoint}"
        
        try:
            response = await self.make_request("GET", url)
            return {
                "success": True,
                "status_code": response.status_code,
                "url": url,
                "response_text": response.text[:500],  # First 500 chars
                "headers": dict(response.headers)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "url": url,
                "status_code": getattr(e, 'response', {}).get('status_code', 'unknown')
            }
    
    async def servicedesk_check_availability(self) -> Dict[str, Any]:
        """Check if Jira Service Management is available and configured"""
        cloud_id = await self.get_cloud_id()
        url = f"https://api.atlassian.com/ex/jira/{cloud_id}/rest/servicedeskapi/servicedesk"
        
        try:
            response = await self.make_request("GET", url, params={"limit": 1})
            service_desks = response.json().get("values", [])
            
            return {
                "available": True,
                "service_desk_count": len(service_desks),
                "service_desks": service_desks,
                "message": f"Jira Service Management is available with {len(service_desks)} service desk(s) configured.",
                "note": "If other servicedesk_ tools fail with 404 errors, you may need to re-authenticate with: authenticate_atlassian()"
            }
        except Exception as e:
            return {
                "available": False,
                "service_desk_count": 0,
                "service_desks": [],
                "message": f"Jira Service Management not available: {str(e)}"
            }


import functools

def handle_atlassian_errors(func):
    """Decorator to convert AtlassianError to ValueError for MCP compatibility."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except AtlassianError as e:
            # Convert structured error to simple ValueError for MCP
            error_msg = f"{e} [Error Code: {e.error_code}]"
            if e.troubleshooting:
                error_msg += f" Troubleshooting: {'; '.join(e.troubleshooting)}"
            if e.suggested_actions:
                error_msg += f" Suggested actions: {'; '.join(e.suggested_actions)}"
            raise ValueError(error_msg)
    return wrapper


# Initialize MCP server
mcp = FastMCP("Atlassian Cloud")

# Global client instance
atlassian_client: Optional[AtlassianClient] = None


@mcp.tool()
async def authenticate_atlassian() -> str:
    """Start seamless Atlassian OAuth authentication flow."""
    if not atlassian_client:
        raise ValueError("Atlassian client not initialized")
    
    try:
        await atlassian_client.seamless_oauth_flow()
        return "✅ Authentication successful! You can now use Atlassian tools."
    except Exception as e:
        return f"❌ Authentication failed: {str(e)}"


@mcp.tool()
async def jira_search(jql: str, max_results: int = 50) -> List[Dict[str, Any]]:
    """Search Jira issues using JQL (Jira Query Language).
    
    Examples:
    - "assignee = currentUser() AND status != Done" - My open issues
    - "project = PROJ AND created >= -7d" - Recent issues in project
    - "text ~ 'bug' ORDER BY created DESC" - Issues containing 'bug'
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.jira_search(jql, max_results)


@mcp.tool()
async def jira_get_issue(issue_key: str) -> Dict[str, Any]:
    """Get detailed information about a specific Jira issue."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.jira_get_issue(issue_key)


@mcp.tool()
async def jira_create_issue(project_key: str, summary: str, description: str, issue_type: str = "Task") -> Dict[str, Any]:
    """Create a new Jira issue.
    
    Args:
        project_key: The project key (e.g., 'PROJ', 'DEV')
        summary: Brief title of the issue
        description: Detailed description of the issue
        issue_type: Type of issue (Task, Story, Bug, etc.)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.jira_create_issue(project_key, summary, description, issue_type)


@mcp.tool()
async def jira_update_issue(issue_key: str, summary: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    """Update an existing Jira issue."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.jira_update_issue(issue_key, summary, description)


@mcp.tool()
async def jira_add_comment(issue_key: str, comment: str) -> Dict[str, Any]:
    """Add a comment to a Jira issue."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.jira_add_comment(issue_key, comment)


@mcp.tool()
async def confluence_search(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Search Confluence pages and content.
    
    Args:
        query: Search term to find in page titles and content
        limit: Maximum number of results to return
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_search(query, limit)


@mcp.tool()
async def confluence_get_page(page_id: str) -> Dict[str, Any]:
    """Get detailed content of a specific Confluence page."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page(page_id)


@mcp.tool()
async def confluence_create_page(space_key: str, title: str, content: str, parent_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a new Confluence page.
    
    Args:
        space_key: The space key where to create the page (e.g., 'PROJ', 'DOC')
        title: Title of the new page
        content: HTML content of the page (use Confluence storage format)
        parent_id: Optional parent page ID to create as a child page
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_create_page(space_key, title, content, parent_id)


@mcp.tool()
async def confluence_update_page(page_id: str, title: str, content: str, version: int) -> Dict[str, Any]:
    """Update an existing Confluence page.
    
    Args:
        page_id: ID of the page to update
        title: New title for the page
        content: New HTML content (use Confluence storage format)
        version: Current version number of the page (get from confluence_get_page)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_update_page(page_id, title, content, version)


# Phase 1: Space Management Tools
@mcp.tool()
async def confluence_list_spaces(limit: int = 25, space_type: Optional[str] = None, status: str = "current") -> List[Dict[str, Any]]:
    """List Confluence spaces.
    
    Args:
        limit: Maximum number of spaces to return (1-250, default: 25)
        space_type: Filter by type: 'global', 'collaboration', 'knowledge_base', 'personal'
        status: Filter by status: 'current', 'archived' (default: 'current')
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_list_spaces(limit, space_type, status)


@mcp.tool()
async def confluence_get_space(space_id: str, include_icon: bool = False) -> Dict[str, Any]:
    """Get detailed information about a specific Confluence space.
    
    Args:
        space_id: ID of the space to retrieve
        include_icon: Whether to include space icon data
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_space(space_id, include_icon)


@mcp.tool()
async def confluence_get_space_pages(space_id: str, limit: int = 25, status: str = "current") -> List[Dict[str, Any]]:
    """Get pages in a specific Confluence space.
    
    Args:
        space_id: ID of the space to get pages from
        limit: Maximum number of pages to return (1-250, default: 25)
        status: Filter by status: 'current', 'archived' (default: 'current')
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_space_pages(space_id, limit, status)


# Phase 2: Enhanced Search & Discovery Tools
@mcp.tool()
async def confluence_search_content(query: str, limit: int = 25, space_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """Advanced search across Confluence content.
    
    Args:
        query: Search term to find in page titles and content
        limit: Maximum number of results to return (1-250, default: 25)
        space_id: Optional space ID to limit search to specific space
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_search_content(query, limit, space_id)


@mcp.tool()
async def confluence_get_page_children(page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Get child pages of a specific Confluence page.
    
    Args:
        page_id: ID of the parent page
        limit: Maximum number of child pages to return (1-250, default: 25)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page_children(page_id, limit)


# Phase 3: Comments & Collaboration Tools
@mcp.tool()
async def confluence_get_page_comments(page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Get comments for a specific Confluence page.
    
    Args:
        page_id: ID of the page to get comments for
        limit: Maximum number of comments to return (1-250, default: 25)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page_comments(page_id, limit)


@mcp.tool()
async def confluence_add_comment(page_id: str, comment: str, parent_comment_id: Optional[str] = None) -> Dict[str, Any]:
    """Add a comment to a Confluence page.
    
    Args:
        page_id: ID of the page to comment on
        comment: Comment text (HTML/storage format)
        parent_comment_id: Optional ID of parent comment for replies
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_add_comment(page_id, comment, parent_comment_id)


@mcp.tool()
async def confluence_get_comment(comment_id: str) -> Dict[str, Any]:
    """Get a specific Confluence comment by ID.
    
    Args:
        comment_id: ID of the comment to retrieve
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_comment(comment_id)


# Phase 4: Labels & Organization Tools
@mcp.tool()
async def confluence_get_page_labels(page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Get labels for a specific Confluence page.
    
    Args:
        page_id: ID of the page to get labels for
        limit: Maximum number of labels to return (1-250, default: 25)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page_labels(page_id, limit)


@mcp.tool()
async def confluence_search_by_label(label_id: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Find Confluence pages with a specific label.
    
    Args:
        label_id: ID of the label to search for
        limit: Maximum number of pages to return (1-250, default: 25)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_search_by_label(label_id, limit)


@mcp.tool()
async def confluence_list_labels(limit: int = 25, prefix: Optional[str] = None) -> List[Dict[str, Any]]:
    """List all Confluence labels with optional filtering.
    
    Args:
        limit: Maximum number of labels to return (1-250, default: 25)
        prefix: Optional prefix to filter labels by ('my', 'team', 'global', 'system')
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_list_labels(limit, prefix)


# Phase 5: Attachments Tools
@mcp.tool()
async def confluence_get_page_attachments(page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Get attachments for a specific Confluence page.
    
    Args:
        page_id: ID of the page to get attachments for
        limit: Maximum number of attachments to return (1-250, default: 25)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page_attachments(page_id, limit)


@mcp.tool()
async def confluence_get_attachment(attachment_id: str) -> Dict[str, Any]:
    """Get details of a specific Confluence attachment.
    
    Args:
        attachment_id: ID of the attachment to retrieve
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_attachment(attachment_id)


# Phase 6: Version History Tools
@mcp.tool()
async def confluence_get_page_versions(page_id: str, limit: int = 25) -> List[Dict[str, Any]]:
    """Get version history for a Confluence page.
    
    Args:
        page_id: ID of the page to get version history for
        limit: Maximum number of versions to return (1-250, default: 25)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page_versions(page_id, limit)


@mcp.tool()
async def confluence_get_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    """Get a specific version of a Confluence page.
    
    Args:
        page_id: ID of the page
        version_number: Version number to retrieve
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.confluence_get_page_version(page_id, version_number)


@mcp.tool()
async def servicedesk_get_requests(service_desk_id: Optional[str] = None, limit: int = 50, start: int = 0) -> List[Dict[str, Any]]:
    """Get service desk requests with pagination support.
    
    Args:
        service_desk_id: Optional service desk ID to filter requests
        limit: Maximum number of requests to return (default: 50, max: 100)
        start: Starting index for pagination (default: 0)
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_requests(service_desk_id, limit, start)


@mcp.tool()
async def servicedesk_get_request(issue_key: str) -> Dict[str, Any]:
    """Get detailed information about a specific service desk request."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request(issue_key)


@mcp.tool()
async def servicedesk_create_request(service_desk_id: str, request_type_id: str, summary: str, description: str) -> Dict[str, Any]:
    """Create a new service desk request.
    
    Args:
        service_desk_id: ID of the service desk
        request_type_id: ID of the request type
        summary: Brief title of the request
        description: Detailed description of the request
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_create_request(service_desk_id, request_type_id, summary, description)


@mcp.tool()
async def servicedesk_add_comment(issue_key: str, comment: str, public: bool = True) -> Dict[str, Any]:
    """Add a comment to a service desk request.
    
    Args:
        issue_key: The service desk request key
        comment: Comment text to add
        public: Whether the comment is public (default: True) or internal
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_add_comment(issue_key, comment, public)


@mcp.tool()
async def servicedesk_get_request_status(issue_key: str) -> Dict[str, Any]:
    """Get the current status of a service desk request."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_status(issue_key)


@mcp.tool()
async def servicedesk_get_approvals(issue_key: str) -> List[Dict[str, Any]]:
    """Get approval information for a service desk request."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_approvals(issue_key)


@mcp.tool()
async def servicedesk_approve_request(issue_key: str, approval_id: str, decision: str) -> Dict[str, Any]:
    """Approve or decline a service desk request approval.
    
    Args:
        issue_key: The service desk request key
        approval_id: The approval ID to respond to  
        decision: 'approve' or 'decline'
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_approve_request(issue_key, approval_id, decision)


@mcp.tool()
async def servicedesk_get_participants(issue_key: str) -> List[Dict[str, Any]]:
    """Get participants for a service desk request."""
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_participants(issue_key)


@mcp.tool()
async def servicedesk_add_participants(issue_key: str, usernames: List[str]) -> Dict[str, Any]:
    """Add participants to a service desk request.
    
    🚨 CRITICAL: DO NOT call this tool without explicit user confirmation first!
    
    REQUIRED WORKFLOW:
    1. ALWAYS ask user: "Adding participants will subscribe them to notifications for ticket {issue_key}. 
       Users {usernames} will receive emails for all updates and can view/comment on the ticket. 
       Do you want to proceed? (yes/no)"
    2. ONLY call this tool if user explicitly confirms with "yes"
    3. If user says "no" or is unsure, do NOT call this tool
    
    This tool adds users to the ticket's notification list and grants them access.
    
    Args:
        issue_key: The service desk request key
        usernames: List of usernames to add as participants
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_add_participants(issue_key, usernames)


@mcp.tool()
async def servicedesk_manage_notifications(issue_key: str, subscribe: bool) -> Dict[str, Any]:
    """Subscribe or unsubscribe from service desk request notifications.
    
    Args:
        issue_key: The service desk request key
        subscribe: True to subscribe, False to unsubscribe
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_manage_notifications(issue_key, subscribe)


@mcp.tool()
async def servicedesk_debug_request(endpoint: str) -> Dict[str, Any]:
    """Debug Service Management API requests to see actual responses.
    
    Args:
        endpoint: Service desk API endpoint to test (e.g., 'request', 'servicedesk/1/request')
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_debug_request(endpoint)


@mcp.tool()
async def servicedesk_check_availability() -> Dict[str, Any]:
    """Check if Jira Service Management is available and configured on this Atlassian instance.
    
    Use this tool first to verify Service Management is set up before using other servicedesk_ tools.
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_check_availability()


# Phase 2: Critical Missing Tools - Service Desk Discovery
@mcp.tool()
@handle_atlassian_errors
async def servicedesk_list_service_desks(limit: int = 50) -> List[Dict[str, Any]]:
    """List available service desks for creating requests.
    
    Essential for AI agents to discover service desks before creating requests.
    Use this tool to find service desk IDs needed for servicedesk_create_request().
    
    Args:
        limit: Maximum number of service desks to return (default: 50, max: 100)
    
    Returns:
        List of service desk objects with id, projectId, projectName, and projectKey
    
    Example:
        service_desks = await servicedesk_list_service_desks()
        # Use service_desks[0]["id"] for creating requests
        
    Common Errors:
        - "Access denied": User may lack Service Management permissions
        - "Endpoint not found": Missing OAuth scopes - re-authenticate with authenticate_atlassian()
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_list_service_desks(limit)


@mcp.tool()
async def servicedesk_get_service_desk(service_desk_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific service desk.
    
    Args:
        service_desk_id: Service desk identifier (get from servicedesk_list_service_desks)
    
    Returns:
        Service desk object with detailed information
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_service_desk(service_desk_id)


@mcp.tool()
@handle_atlassian_errors
async def servicedesk_list_request_types(service_desk_id: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
    """List available request types for creating service desk requests.
    
    Essential for AI agents to discover request types before creating requests.
    Use this tool to find request type IDs needed for servicedesk_create_request().
    
    Args:
        service_desk_id: Optional service desk ID to filter request types.
                        If None, returns request types from all accessible service desks.
        limit: Maximum number of request types to return (default: 50, max: 100)
    
    Returns:
        List of request type objects with id, name, description, and serviceDeskId
    
    Example:
        # Get all request types
        all_types = await servicedesk_list_request_types()
        
        # Get request types for specific service desk
        it_types = await servicedesk_list_request_types(service_desk_id="10")
        # Use it_types[0]["id"] for creating requests
        
    Common Errors:
        - "Service desk not found": Use servicedesk_list_service_desks() to find valid IDs
        - "Access denied": User may lack Service Management permissions
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_list_request_types(service_desk_id, limit)


@mcp.tool()
async def servicedesk_get_request_type(service_desk_id: str, request_type_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific request type.
    
    Args:
        service_desk_id: Service desk identifier
        request_type_id: Request type identifier
    
    Returns:
        Request type object with detailed information
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_type(service_desk_id, request_type_id)


@mcp.tool()
async def servicedesk_get_request_type_fields(service_desk_id: str, request_type_id: str) -> List[Dict[str, Any]]:
    """Get required and optional fields for a specific request type.
    
    Essential for understanding what fields are needed when creating requests.
    
    Args:
        service_desk_id: Service desk identifier
        request_type_id: Request type identifier
    
    Returns:
        List of field objects with fieldId, name, required, and other metadata
    
    Example:
        fields = await servicedesk_get_request_type_fields("10", "25")
        required_fields = [f for f in fields if f.get("required", False)]
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_type_fields(service_desk_id, request_type_id)


# Phase 2: Enhanced Request Management
@mcp.tool()
async def servicedesk_get_request_comments(issue_key: str, limit: int = 50) -> List[Dict[str, Any]]:
    """Get comments for a service desk request.
    
    Args:
        issue_key: Service desk request key (e.g., "HELP-123")
        limit: Maximum number of comments to return (default: 50)
    
    Returns:
        List of comment objects with body, author, created date, and visibility
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_comments(issue_key, limit)


@mcp.tool()
async def servicedesk_get_request_transitions(issue_key: str) -> List[Dict[str, Any]]:
    """Get available transitions for a service desk request.
    
    Use this to see what status changes are possible for a request.
    
    Args:
        issue_key: Service desk request key (e.g., "HELP-123")
    
    Returns:
        List of transition objects with id, name, and to status
    
    Example:
        transitions = await servicedesk_get_request_transitions("HELP-123")
        # Use transitions[0]["id"] with servicedesk_transition_request()
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_transitions(issue_key)


@mcp.tool()
async def servicedesk_transition_request(issue_key: str, transition_id: str, comment: Optional[str] = None) -> Dict[str, Any]:
    """Transition a service desk request to a new status.
    
    Args:
        issue_key: Service desk request key (e.g., "HELP-123")
        transition_id: ID of the transition to perform (get from servicedesk_get_request_transitions)
        comment: Optional comment to add with the transition
    
    Returns:
        Success confirmation with transition details
    
    Example:
        # First get available transitions
        transitions = await servicedesk_get_request_transitions("HELP-123")
        # Then transition to new status
        result = await servicedesk_transition_request("HELP-123", transitions[0]["id"], "Moving to in progress")
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_transition_request(issue_key, transition_id, comment)


# Phase 3: Advanced Features - MCP Tools

@mcp.tool()
@handle_atlassian_errors
async def servicedesk_get_request_sla(issue_key: str) -> List[Dict[str, Any]]:
    """Get SLA information for a service desk request.
    
    Shows SLA metrics, timing, and breach status for performance monitoring.
    
    Args:
        issue_key: Service desk request key (e.g., "HELP-123")
    
    Returns:
        List of SLA metric objects with timing and status information
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_sla(issue_key)


@mcp.tool()
@handle_atlassian_errors
async def servicedesk_get_sla_metric(issue_key: str, sla_metric_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific SLA metric.
    
    Args:
        issue_key: Service desk request key
        sla_metric_id: SLA metric ID (from servicedesk_get_request_sla)
    
    Returns:
        Detailed SLA metric with timing cycles and breach information
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_sla_metric(issue_key, sla_metric_id)


@mcp.tool()
@handle_atlassian_errors
async def servicedesk_get_request_attachments(issue_key: str) -> List[Dict[str, Any]]:
    """Get attachments for a service desk request.
    
    Args:
        issue_key: Service desk request key (e.g., "HELP-123")
    
    Returns:
        List of attachment objects with filename, size, and download URLs
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_get_request_attachments(issue_key)


@mcp.tool()
@handle_atlassian_errors
async def servicedesk_search_knowledge_base(query: str, service_desk_id: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
    """Search knowledge base articles for relevant information.
    
    Args:
        query: Search query string
        service_desk_id: Optional service desk ID to filter articles
        limit: Maximum articles to return (default: 10, max: 50)
    
    Returns:
        List of knowledge base articles with title, excerpt, and content URLs
    """
    if not atlassian_client or not atlassian_client.config.access_token:
        raise ValueError("Not authenticated. Use authenticate_atlassian tool first.")
    return await atlassian_client.servicedesk_search_knowledge_base(query, service_desk_id, limit)


async def initialize_client():
    """Initialize the Atlassian client."""
    global atlassian_client
    
    site_url = os.getenv("ATLASSIAN_SITE_URL")
    client_id = os.getenv("ATLASSIAN_CLIENT_ID")
    client_secret = os.getenv("ATLASSIAN_CLIENT_SECRET")
    
    if not all([site_url, client_id, client_secret]):
        raise ValueError("ATLASSIAN_SITE_URL, ATLASSIAN_CLIENT_ID, and ATLASSIAN_CLIENT_SECRET must be set")
    
    config = AtlassianConfig(
        site_url=site_url,
        client_id=client_id,
        client_secret=client_secret
    )
    
    atlassian_client = AtlassianClient(config)
    
    # Try to load existing credentials
    if atlassian_client.load_credentials():
        print("✅ Loaded existing Atlassian credentials")
        try:
            # Test credentials
            await atlassian_client.get_headers()
            print("✅ Credentials are valid")
        except Exception:
            print("⚠️ Stored credentials are invalid. Use authenticate_atlassian tool to re-authenticate.")
    else:
        print("🔐 No existing credentials found. Use authenticate_atlassian tool to authenticate.")


def main():
    """Main entry point."""
    try:
        # Initialize client
        asyncio.run(initialize_client())
        
        # Run MCP server
        mcp.run()
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return 1


if __name__ == "__main__":
    main()
