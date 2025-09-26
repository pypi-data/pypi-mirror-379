"""Google Cloud Search API."""


from googleapiclient.discovery import build

from bits.google.services.base import Base


class CloudSearch(Base):
    """CloudBilling class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.cloudsearch = build('cloudsearch', 'v1', credentials=credentials, cache_discovery=False)

    def get_stats(self, params):
        """Return stats."""
        return self.cloudsearch.stats().getIndex(**params).execute().get('stats', [])
