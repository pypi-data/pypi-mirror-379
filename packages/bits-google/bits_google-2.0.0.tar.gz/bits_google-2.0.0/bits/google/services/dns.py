"""Google Cloud DNS API."""

from google.cloud.dns import client
from googleapiclient.discovery import build

from bits.google.services.base import Base


class CloudDNS(Base):
    """CloudDNS class."""

    def __init__(self, credentials=None, project=None):
        """Initialize a class instance."""
        self.dns = build('dns', 'v1', credentials=credentials, cache_discovery=False)
        self.client = client.Client(project)

    def get_managed_zones(self, project):
        """Return list of DNS managed zones."""
        managedZones = self.dns.managedZones()
        request = managedZones.list(project=project)
        return self.get_list_items(managedZones, request, 'managedZones')

    def get_resource_records(self, project, zone):
        """Return a list of resource records for a specific project/zone."""
        resourceRecordSets = self.dns.resourceRecordSets()
        request = resourceRecordSets.list(project=project, managedZone=zone)
        return self.get_list_items(resourceRecordSets, request, 'rrsets')
