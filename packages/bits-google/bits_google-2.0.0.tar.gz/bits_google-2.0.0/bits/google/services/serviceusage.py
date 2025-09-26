"""Service Usage API class file."""

from google.auth.transport.requests import AuthorizedSession

from bits.google.services.base import Base

# from googleapiclient.discovery import build


class ServiceUsage(Base):
    """ServiceUsage API class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.credentials = credentials

        # settings for requests
        self.alpha_base_url = 'https://serviceusage.googleapis.com/v1alpha'
        self.base_url = 'https://serviceusage.googleapis.com/v1'
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.requests = AuthorizedSession(credentials)

    def get_list(self, url, collection, params={}):
        """Return a list of items from a paginated GET request."""
        params['pageToken'] = None
        response = self.requests.get(url, headers=self.headers).json()
        items = response.get(collection, [])
        pageToken = response.get('nextPageToken')
        while pageToken:
            params['pageToken'] = pageToken
            response = self.requests.get(url, headers=self.headers, params=params).json()
            items.extend(response.get(collection, []))
            pageToken = response.get('nextPageToken')
        return items

    def get_project_services(self, project):
        """Return a list of services enabled in the project."""
        url = f'{self.base_url}/projects/{project}/services?filter=state:ENABLED'
        return self.get_list(url, 'services')

    def get_folder_service_quotas(self, folder, service):
        """Return a list of quotas for a service in a folder."""
        resource = f'folders/{folder}'
        return self.get_resource_service_quotas(resource, service)

    def get_organization_service_quotas(self, organization, service):
        """Return a list of quotas for a service in an organization."""
        resource = f'organizations/{organization}'
        return self.get_resource_service_quotas(resource, service)

    def get_project_service_quotas(self, project, service):
        """Return a list of quotas for a service in a project."""
        resource = f'projects/{project}'
        return self.get_resource_service_quotas(resource, service)

    def get_operation(self, name):
        """Return an operation by name."""
        url = f'{self.alpha_base_url}/{name}'
        return self.requests.get(url, headers=self.headers).json()

    def get_resource_service_quotas(self, resource, service):
        """Return a list of quotas for a resource."""
        url = f'{self.alpha_base_url}/{resource}/services/{service}/quotaMetrics'
        return self.get_list(url, 'metrics')

    def set_admin_override(self, resource, value=None, force=False, location=None):
        """Set an admin override on a resource."""
        url = f'{self.alpha_base_url}/{resource}:setAdminOverride'
        body = {
            'force': force,
            'location': location,
            'override_value': value,
        }
        return self.requests.post(url, headers=self.headers, json=body).json()

    def set_consumer_override(self, resource, value=None, force=False, location=None):
        """Set a consumer override on a resource."""
        url = f'{self.alpha_base_url}/{resource}:setConsumerOverride'
        body = {
            'force': force,
            'location': location,
            'override_value': value,
        }
        return self.requests.post(url, headers=self.headers, json=body).json()
