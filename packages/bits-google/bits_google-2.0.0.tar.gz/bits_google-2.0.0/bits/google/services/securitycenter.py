"""Security Center API class file."""

from googleapiclient.discovery import build

from bits.google.services.base import Base


class SecurityCenter(Base):
    """SecurityCenter class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.securitycenter = build(
            'securitycenter',
            'v1beta1',
            credentials=credentials,
            cache_discovery=False,
        )

    def get_organization_assets(
        self,
        organization,
        filter=None,
        orderBy=None,
        readTime=None,
        compareDuration=None,
        fieldMask=None,
        pageSize=1000,
    ):
        """Return list of assets."""
        params = {
            'parent': f'organizations/{organization}',
            'filter': filter,
            'orderBy': orderBy,
            'readTime': readTime,
            'compareDuration': compareDuration,
            'fieldMask': fieldMask,
            'pageSize': pageSize,
        }
        assets = self.securitycenter.organizations().assets()
        request = assets.list(**params)
        return self.get_list_items(assets, request, 'listAssetsResults')
