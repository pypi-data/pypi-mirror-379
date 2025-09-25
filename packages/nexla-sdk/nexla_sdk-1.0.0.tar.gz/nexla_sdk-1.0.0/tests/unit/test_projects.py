"""Unit tests for projects resource."""
import pytest
from unittest.mock import MagicMock
from nexla_sdk.models.projects.responses import Project, ProjectDataFlow
from nexla_sdk.models.projects.requests import ProjectCreate, ProjectUpdate, ProjectFlowList, ProjectFlowIdentifier
from nexla_sdk.models.flows.responses import FlowResponse
from nexla_sdk.exceptions import ServerError
from nexla_sdk.http_client import HttpClientError
from tests.utils.fixtures import create_test_client
from tests.utils.mock_builders import MockResponseBuilder, MockDataFactory
from tests.utils.assertions import NexlaAssertions


class TestProjectsResource:
    """Test cases for ProjectsResource."""

    @pytest.fixture
    def mock_client(self):
        """Create a test client with mocked HTTP."""
        return create_test_client()

    @pytest.fixture
    def assertions(self):
        """Create assertions helper."""
        return NexlaAssertions()

    def test_list_projects(self, mock_client, assertions):
        """Test listing projects."""
        # Arrange
        mock_data = [MockResponseBuilder.project() for _ in range(2)]
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        # Act
        projects = mock_client.projects.list()
        
        # Assert
        assert len(projects) == 2
        assert all(isinstance(project, Project) for project in projects)
        
        # Verify first project structure
        assertions.assert_project_response(projects[0], mock_data[0])
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'GET'
        assert '/projects' in call_args[0][1]

    def test_list_projects_with_parameters(self, mock_client):
        """Test listing projects with query parameters."""
        # Arrange
        mock_data = [MockResponseBuilder.project()]
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        # Act
        projects = mock_client.projects.list(page=2, per_page=10, access_role="collaborator")
        
        # Assert
        assert len(projects) == 1
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'GET'
        assert '/projects' in call_args[0][1]
        assert 'params' in call_args[1]

    def test_list_projects_with_expand(self, mock_client):
        """Test listing projects with expand parameter."""
        # Arrange
        factory = MockDataFactory()
        project_data = factory.create_mock_project()
        project_data['data_flows'] = [factory.create_mock_project_data_flow() for _ in range(2)]
        project_data['flows'] = [factory.create_mock_project_data_flow() for _ in range(2)]
        mock_client.http_client.request = MagicMock(return_value=[project_data])
        
        # Act
        projects = mock_client.projects.list(expand=True)
        
        # Assert
        assert len(projects) == 1
        assert len(projects[0].data_flows) == 2
        assert len(projects[0].flows) == 2
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'GET'
        assert '/projects' in call_args[0][1]
        assert 'params' in call_args[1]

    def test_get_project(self, mock_client, assertions):
        """Test getting a single project."""
        # Arrange
        project_id = 123
        mock_data = MockResponseBuilder.project()
        mock_data['id'] = project_id
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        # Act
        project = mock_client.projects.get(project_id)
        
        # Assert
        assert isinstance(project, Project)
        assert project.id == project_id
        assertions.assert_project_response(project, mock_data)
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'GET'
        assert f'/projects/{project_id}' in call_args[0][1]

    def test_get_project_with_expand(self, mock_client):
        """Test getting project with expand parameter."""
        # Arrange
        project_id = 123
        mock_data = MockResponseBuilder.project()
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        # Act
        project = mock_client.projects.get(project_id, expand=True)
        
        # Assert
        assert isinstance(project, Project)
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'GET'
        assert f'/projects/{project_id}' in call_args[0][1]
        assert 'params' in call_args[1]

    def test_create_project(self, mock_client, assertions):
        """Test creating a project."""
        # Arrange
        mock_data = MockResponseBuilder.project()
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        project_data = ProjectCreate(
            name="Test Project",
            description="Test project description",
            data_flows=[
                ProjectFlowIdentifier(data_source_id=123),
                ProjectFlowIdentifier(data_set_id=456)
            ]
        )
        
        # Act
        project = mock_client.projects.create(project_data)
        
        # Assert
        assert isinstance(project, Project)
        assertions.assert_project_response(project, mock_data)
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'POST'
        assert '/projects' in call_args[0][1]
        assert 'json' in call_args[1]

    def test_update_project(self, mock_client):
        """Test updating a project."""
        # Arrange
        project_id = 123
        mock_data = MockResponseBuilder.project()
        mock_data['id'] = project_id
        mock_data['name'] = "Updated Project"
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        update_data = ProjectUpdate(
            name="Updated Project",
            description="Updated description"
        )
        
        # Act
        project = mock_client.projects.update(project_id, update_data)
        
        # Assert
        assert isinstance(project, Project)
        assert project.name == "Updated Project"
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'PUT'
        assert f'/projects/{project_id}' in call_args[0][1]

    def test_delete_project(self, mock_client):
        """Test deleting a project."""
        # Arrange
        project_id = 123
        mock_client.http_client.request = MagicMock(return_value={"status": "deleted"})
        
        # Act
        result = mock_client.projects.delete(project_id)
        
        # Assert
        assert result == {"status": "deleted"}
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'DELETE'
        assert f'/projects/{project_id}' in call_args[0][1]

    def test_get_flows(self, mock_client):
        """Test getting flows in a project."""
        # Arrange
        project_id = 123
        mock_data = {
            "flows": [{
                "id": 1,
                "origin_node_id": 1,
                "parent_node_id": None,
                "data_source_id": None,
                "data_set_id": None,
                "data_sink_id": None,
                "status": None,
                "project_id": None,
                "flow_type": None,
                "ingestion_mode": None,
                "name": "test flow",
                "description": None,
                "children": None
            }],
            "data_sources": [],
            "data_sets": [],
            "data_sinks": []
        }
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        # Act
        flows = mock_client.projects.get_flows(project_id)
        
        # Assert
        assert isinstance(flows, FlowResponse)
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'GET'
        assert f'/projects/{project_id}/flows' in call_args[0][1]

    def test_search_flows(self, mock_client):
        """Test searching flows in a project."""
        # Arrange
        project_id = 123
        filters = [{"field": "name", "operator": "contains", "value": "test"}]
        mock_data = {
            "flows": [{
                "id": 1,
                "origin_node_id": 1,
                "parent_node_id": None,
                "data_source_id": None,
                "data_set_id": None,
                "data_sink_id": None,
                "status": None,
                "project_id": None,
                "flow_type": None,
                "ingestion_mode": None,
                "name": "test flow",
                "description": None,
                "children": None
            }],
            "data_sources": [],
            "data_sets": [],
            "data_sinks": []
        }
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        # Act
        flows = mock_client.projects.search_flows(project_id, filters)
        
        # Assert
        assert isinstance(flows, FlowResponse)
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'POST'
        assert f'/projects/{project_id}/flows/search' in call_args[0][1]

    def test_add_data_flows(self, mock_client):
        """Test adding data flows to a project."""
        # Arrange
        project_id = 123
        factory = MockDataFactory()
        mock_data = [factory.create_mock_project_data_flow() for _ in range(2)]
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        flows = ProjectFlowList(
            data_flows=[
                ProjectFlowIdentifier(data_source_id=456),
                ProjectFlowIdentifier(data_set_id=789)
            ]
        )
        
        # Act
        result = mock_client.projects.add_data_flows(project_id, flows)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(flow, ProjectDataFlow) for flow in result)
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'PUT'
        assert f'/projects/{project_id}/data_flows' in call_args[0][1]

    def test_replace_data_flows(self, mock_client):
        """Test replacing data flows in a project."""
        # Arrange
        project_id = 123
        factory = MockDataFactory()
        mock_data = [factory.create_mock_project_data_flow()]
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        flows = ProjectFlowList(
            data_flows=[ProjectFlowIdentifier(data_source_id=999)]
        )
        
        # Act
        result = mock_client.projects.replace_data_flows(project_id, flows)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 1
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'POST'
        assert f'/projects/{project_id}/data_flows' in call_args[0][1]

    def test_remove_data_flows(self, mock_client):
        """Test removing data flows from a project."""
        # Arrange
        project_id = 123
        factory = MockDataFactory()
        mock_data = [factory.create_mock_project_data_flow()]
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        flows = ProjectFlowList(
            data_flows=[ProjectFlowIdentifier(data_source_id=456)]
        )
        
        # Act
        result = mock_client.projects.remove_data_flows(project_id, flows)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 1
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'DELETE'
        assert f'/projects/{project_id}/data_flows' in call_args[0][1]

    def test_remove_all_data_flows(self, mock_client):
        """Test removing all data flows from a project."""
        # Arrange
        project_id = 123
        mock_client.http_client.request = MagicMock(return_value=[])
        
        # Act
        result = mock_client.projects.remove_data_flows(project_id)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 0
        
        # Verify the request
        mock_client.http_client.request.assert_called_once()
        call_args = mock_client.http_client.request.call_args
        assert call_args[0][0] == 'DELETE'
        assert f'/projects/{project_id}/data_flows' in call_args[0][1]

    def test_backward_compatibility_methods(self, mock_client):
        """Test backward compatibility methods."""
        # Arrange
        project_id = 123
        factory = MockDataFactory()
        mock_data = [factory.create_mock_project_data_flow()]
        mock_client.http_client.request = MagicMock(return_value=mock_data)
        
        flows = ProjectFlowList(
            data_flows=[ProjectFlowIdentifier(data_source_id=123)]
        )
        
        # Test add_flows (deprecated)
        result = mock_client.projects.add_flows(project_id, flows)
        assert isinstance(result, list)
        assert len(result) == 1
        
        # Reset mock for next call
        mock_client.http_client.request.reset_mock()
        mock_client.http_client.request.return_value = mock_data
        
        # Test replace_flows (deprecated)
        result = mock_client.projects.replace_flows(project_id, flows)
        assert isinstance(result, list)
        assert len(result) == 1
        
        # Reset mock for next call
        mock_client.http_client.request.reset_mock()
        mock_client.http_client.request.return_value = mock_data
        
        # Test remove_flows (deprecated)
        result = mock_client.projects.remove_flows(project_id, flows)
        assert isinstance(result, list)
        assert len(result) == 1

    def test_http_error_handling(self, mock_client):
        """Test HTTP error handling."""
        # Arrange
        project_id = 999
        mock_client.http_client.request = MagicMock(
            side_effect=HttpClientError(
                "API Error",
                status_code=500,
                response={"message": "Internal server error"}
            )
        )
        
        # Act & Assert
        with pytest.raises(ServerError):
            mock_client.projects.get(project_id)

    def test_not_found_error_handling(self, mock_client):
        """Test not found error handling."""
        # Arrange
        project_id = 999
        mock_client.http_client.request = MagicMock(
            side_effect=HttpClientError(
                "Project not found",
                status_code=404,
                response={"message": "Project not found"}
            )
        )
        
        # Act & Assert
        with pytest.raises(ServerError):  # This will be converted to NotFoundError by client
            mock_client.projects.get(project_id)

    def test_validation_error_handling(self, mock_client):
        """Test validation error handling."""
        # Arrange - Test creating project with invalid data that will fail Pydantic validation
        
        # Act & Assert
        with pytest.raises(Exception):  # Pydantic will raise validation error
            # Missing required 'name' field will fail validation
            ProjectCreate(description="Test")  # Missing name field should fail validation

    def test_empty_list_response(self, mock_client):
        """Test empty list response."""
        # Arrange
        mock_client.http_client.request = MagicMock(return_value=[])
        
        # Act
        projects = mock_client.projects.list()
        
        # Assert
        assert isinstance(projects, list)
        assert len(projects) == 0 