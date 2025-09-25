"""Lookups resource implementation."""
from typing import List, Dict, Any, Union
from nexla_sdk.resources.base_resource import BaseResource
from nexla_sdk.models.lookups.responses import Lookup
from nexla_sdk.models.lookups.requests import LookupCreate, LookupUpdate, LookupEntriesUpsert


class LookupsResource(BaseResource):
    """Resource for managing lookups (data maps)."""
    
    def __init__(self, client):
        super().__init__(client)
        self._path = "/data_maps"
        self._model_class = Lookup
    
    def list(self, **kwargs) -> List[Lookup]:
        """
        List all lookups.
        
        Args:
            **kwargs: Additional parameters (page, per_page, access_role, etc.)
        
        Returns:
            List of lookups
        """
        return super().list(**kwargs)
    
    def get(self, data_map_id: int, expand: bool = False) -> Lookup:
        """
        Get single lookup by ID.
        
        Args:
            data_map_id: Lookup ID
            expand: Include expanded references
        
        Returns:
            Lookup instance
        """
        return super().get(data_map_id, expand)
    
    def create(self, data: LookupCreate) -> Lookup:
        """
        Create new lookup.
        
        Args:
            data: Lookup creation data
        
        Returns:
            Created lookup
        """
        return super().create(data)
    
    def update(self, data_map_id: int, data: LookupUpdate) -> Lookup:
        """
        Update lookup.
        
        Args:
            data_map_id: Lookup ID
            data: Updated lookup data
        
        Returns:
            Updated lookup
        """
        return super().update(data_map_id, data)
    
    def delete(self, data_map_id: int) -> Dict[str, Any]:
        """
        Delete lookup.
        
        Args:
            data_map_id: Lookup ID
        
        Returns:
            Response with status
        """
        return super().delete(data_map_id)

    def upsert_entries(self,
                       data_map_id: int,
                       entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Upsert entries in a lookup.
        
        Args:
            data_map_id: Lookup ID
            entries: List of entries to upsert
        
        Returns:
            Response with entry results
        """
        path = f"{self._path}/{data_map_id}/entries"
        
        # Create request model
        request = LookupEntriesUpsert(entries=entries)
        
        return self._make_request('PUT', path, json=request.to_dict())
    
    def get_entries(self,
                    data_map_id: int,
                    entry_keys: Union[str, List[str]]) -> List[Dict[str, Any]]:
        """
        Get specific entries from a lookup.
        
        Args:
            data_map_id: Lookup ID
            entry_keys: Single key or list of keys to retrieve
        
        Returns:
            List of matching entries
        """
        if isinstance(entry_keys, list):
            keys_str = ','.join(str(key) for key in entry_keys)
        else:
            keys_str = str(entry_keys)
        
        path = f"/data_maps/{data_map_id}/entries/{keys_str}"
        return self._make_request('GET', path)
    
    def delete_entries(self,
                       data_map_id: int,
                       entry_keys: Union[str, List[str]]) -> Dict[str, Any]:
        """
        Delete specific entries from a lookup.
        
        Args:
            data_map_id: Lookup ID
            entry_keys: Single key or list of keys to delete
        
        Returns:
            Response with deletion results
        """
        if isinstance(entry_keys, list):
            keys_str = ','.join(str(key) for key in entry_keys)
        else:
            keys_str = str(entry_keys)
        
        path = f"/data_maps/{data_map_id}/entries/{keys_str}"
        return self._make_request('DELETE', path)
