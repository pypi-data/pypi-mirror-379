"""Base service class file."""


class Base:
    """Base service class."""

    def get_list_items(self, method, request, name):
        """Return items from a Google list/list_next cycle."""
        items = []
        while request is not None:
            response = request.execute()
            items += response.get(name, [])
            request = method.list_next(request, response)
        return items

    def get_list_items_iterator(self, method, request, name):
        """Return items from a Google list/list_next cycle as an interator."""
        while request is not None:
            response = request.execute()
            items = response.get(name, [])
            yield from items
            request = method.list_next(request, response)
