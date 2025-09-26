"""Google Datastore API client."""

from google.cloud import datastore

from bits.google.services.base import Base
from bits.helpers import chunks


class Datastore(Base):
    """Datastore class."""

    def __init__(self, project, credentials=None):
        """Initialize a class instance."""
        # uses application default credentials.
        self.client = datastore.Client(project, credentials=credentials)
        self.datastore = datastore

    def _get_entities_to_add(self, old, new):
        """Return al ist of entities to add."""
        add = []
        for key in new:
            if key not in old:
                add.append(new[key])
        return add

    def _get_entities_to_delete(self, old, new):
        """Return a list of entities to delete."""
        delete = []
        for key in old:
            if key not in new:
                delete.append(old[key].key)
        return delete

    def _get_entities_to_update(self, old, new):
        """Return a list of entities to update."""
        update = []
        for key in new:
            if key not in old:
                continue
            if old[key] != new[key]:
                update.append(new[key])
        return update

    def create_entities(self, records, kind, key='id'):
        """Return a dict of datastore entities."""
        entities = {}
        for record in records:
            # get the key value for the entity
            rid = record[key]
            # create the entity key
            entity_key = self.client.key(kind, rid)
            # create entity
            entity = self.datastore.Entity(entity_key)
            # update entity data
            for k in record:
                entity[k] = record[k]
            # store entity in the dictionary
            entities[rid] = entity
        return entities

    def list_entities(self, kind):
        """Return a list of all entities of a given kind."""
        query = self.client.query(kind=kind)
        return list(query.fetch())

    def list_entities_dict(self, kind):
        """Return a dict of all entities of a given kind."""
        entities = {}
        for entity in self.list_entities(kind):
            entity_key = entity.key.id
            if not entity_key:
                entity_key = entity.key.name
            entities[entity_key] = entity
        return entities

    def update_collection(self, kind, old, new):
        """Update a datastore collection."""
        # get entities to add
        add = self._get_entities_to_add(old, new)
        print(f'{kind} entities to add: {len(add)}')

        # get entities to delete
        delete = self._get_entities_to_delete(old, new)
        print(f'{kind} entities to delete: {len(delete)}')

        # get entities to update
        update = self._get_entities_to_update(old, new)
        print(f'{kind} entities to update: {len(update)}')

        # add new entities
        done = 0
        for chunk in chunks(add, 500):
            done += len(chunk)
            print(f'Adding {len(chunk)} [{done}/{len(add)}] {kind} entities...')
            self.client.put_multi(chunk)

        # delete extra entities
        done = 0
        for chunk in chunks(delete, 500):
            done += len(chunk)
            print(f'Deleting {len(chunk)} [{done}/{len(delete)}] {kind} entities...')
            self.client.delete_multi(chunk)

        # update changed entities
        done = 0
        for chunk in chunks(update, 500):
            done += len(chunk)
            print(f'Updating {len(chunk)} [{done}/{len(update)}] {kind} entities...')
            self.client.put_multi(chunk)
