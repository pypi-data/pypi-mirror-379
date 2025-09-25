from typing import List, Optional, Dict, Any
from nexla_sdk.resources.base_resource import BaseResource
from nexla_sdk.models.users.responses import User, UserExpanded, UserSettings
from nexla_sdk.models.users.requests import UserCreate, UserUpdate
from nexla_sdk.models.metrics.enums import UserMetricResourceType


class UsersResource(BaseResource):
    """Resource for managing users."""
    
    def __init__(self, client):
        super().__init__(client)
        self._path = "/users"
        self._model_class = User
    
    def list(self, expand: bool = False, **kwargs) -> List[User]:
        """
        List all users.
        
        Args:
            expand: Include expanded information
            **kwargs: Additional parameters (page, per_page, access_role, etc.)
        
        Returns:
            List of users
        """
        if expand:
            response = self._make_request('GET', f"{self._path}?expand=1", params=kwargs)
            return [UserExpanded(**item) for item in response]
        
        return super().list(**kwargs)
    
    def get(self, user_id: int, expand: bool = False) -> User:
        """
        Get user by ID.
        
        Args:
            user_id: User ID
            expand: Include expanded information
        
        Returns:
            User object
        """
        if expand:
            path = f"{self._path}/{user_id}?expand=1"
            response = self._make_request('GET', path)
            return UserExpanded(**response)
        
        return super().get(user_id, expand=False)
    
    def create(self, data: UserCreate) -> User:
        """
        Create new user.
        
        Args:
            data: User creation data
        
        Returns:
            Created user
        """
        return super().create(data)
    
    def update(self, user_id: int, data: UserUpdate) -> User:
        """
        Update user.
        
        Args:
            user_id: User ID
            data: Updated user data
        
        Returns:
            Updated user
        """
        return super().update(user_id, data)
    
    def delete(self, user_id: int) -> Dict[str, Any]:
        """
        Delete user.
        
        Args:
            user_id: User ID
        
        Returns:
            Response with status
        """
        return super().delete(user_id)
    
    def get_settings(self) -> List[UserSettings]:
        """
        Get current user's settings.
        
        Returns:
            List of user settings
        """
        path = "/user_settings"
        response = self._make_request('GET', path)
        return [UserSettings(**item) for item in response]
    
    def get_quarantine_settings(self, user_id: int) -> Dict[str, Any]:
        """
        Get quarantine data export settings for user.
        
        Args:
            user_id: User ID
        
        Returns:
            Quarantine settings
        """
        path = f"{self._path}/{user_id}/quarantine_settings"
        return self._make_request('GET', path)
    
    def create_quarantine_settings(self,
                                   user_id: int,
                                   data_credentials_id: int,
                                   config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create quarantine data export settings.
        
        Args:
            user_id: User ID
            data_credentials_id: Credential ID for export location
            config: Configuration including cron schedule and path
        
        Returns:
            Created settings
        """
        path = f"{self._path}/{user_id}/quarantine_settings"
        data = {
            'data_credentials_id': data_credentials_id,
            'config': config
        }
        return self._make_request('POST', path, json=data)
    
    def update_quarantine_settings(self,
                                   user_id: int,
                                   data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update quarantine data export settings.
        
        Args:
            user_id: User ID
            data: Updated settings
        
        Returns:
            Updated settings
        """
        path = f"{self._path}/{user_id}/quarantine_settings"
        return self._make_request('PUT', path, json=data)
    
    def delete_quarantine_settings(self, user_id: int) -> Dict[str, Any]:
        """
        Delete quarantine data export settings.
        
        Args:
            user_id: User ID
        
        Returns:
            Response status
        """
        path = f"{self._path}/{user_id}/quarantine_settings"
        return self._make_request('DELETE', path)
    
    def get_transferable_resources(self, user_id: int, org_id: int) -> Dict[str, Any]:
        """
        Get a list of resources owned by a user that can be transferred.
        
        Args:
            user_id: The ID of the user whose resources are being checked
            org_id: The ID of the organization context
            
        Returns:
            A dictionary of transferable resources by type
        """
        path = f"{self._path}/{user_id}/transferable"
        params = {'org_id': org_id}
        return self._make_request('GET', path, params=params)
        
    def transfer_resources(self, user_id: int, org_id: int, delegate_owner_id: int) -> Dict[str, Any]:
        """
        Transfer a user's resources to another user within an organization.
        
        Args:
            user_id: The ID of the user whose resources are being transferred
            org_id: The ID of the organization context
            delegate_owner_id: The ID of the user to whom resources will be transferred
            
        Returns:
            A dictionary confirming the transfer details
        """
        path = f"{self._path}/{user_id}/transfer"
        data = {
            'org_id': org_id,
            'delegate_owner_id': delegate_owner_id
        }
        return self._make_request('PUT', path, json=data)
        
    def get_account_metrics(self,
                            user_id: int,
                            from_date: str,
                            to_date: Optional[str] = None,
                            org_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Get total account metrics for user.
        
        Args:
            user_id: User ID
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (optional)
            org_id: Organization ID (for users in multiple orgs)
        
        Returns:
            Account metrics
        """
        path = f"{self._path}/{user_id}/flows/account_metrics"
        params = {'from': from_date}
        if to_date:
            params['to'] = to_date
        if org_id:
            params['org_id'] = org_id
        
        return self._make_request('GET', path, params=params)
    
    def get_dashboard_metrics(self,
                              user_id: int,
                              access_role: Optional[str] = None) -> Dict[str, Any]:
        """
        Get 24 hour flow stats for user.
        
        Args:
            user_id: User ID
            access_role: Filter by access role
        
        Returns:
            Dashboard metrics
        """
        path = f"{self._path}/{user_id}/flows/dashboard"
        params = {}
        if access_role:
            params['access_role'] = access_role
        
        return self._make_request('GET', path, params=params)
    
    def get_daily_metrics(self,
                          user_id: int,
                          resource_type: UserMetricResourceType,
                          from_date: str,
                          to_date: Optional[str] = None,
                          org_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Get daily data processing metrics for a user.
        
        Args:
            user_id: User ID
            resource_type: Type of resource (SOURCE, SINK)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (optional)
            org_id: Organization ID (optional)
        
        Returns:
            Daily metrics data
        """
        path = f"{self._path}/{user_id}/metrics"
        params = {
            'resource_type': resource_type,
            'from': from_date,
            'aggregate': 1
        }
        if to_date:
            params['to'] = to_date
        if org_id:
            params['org_id'] = org_id
        
        return self._make_request('GET', path, params=params)
