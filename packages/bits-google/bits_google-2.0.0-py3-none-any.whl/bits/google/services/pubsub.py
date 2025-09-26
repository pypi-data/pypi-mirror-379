"""Google PubSub API."""

import base64
import json

from google.cloud import pubsub_v1
from googleapiclient.discovery import build

from bits.google.services.base import Base


class PubSub(Base):
    """PubSub class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.pubsub = build('pubsub', 'v1', credentials=credentials, cache_discovery=False)
        self.pubsub_v1 = pubsub_v1

    def get_pubsub_message_json_data(self, data):
        """Return the json body from a pubsub message."""
        # get the body text
        body_text = None
        if 'data' in data:
            body_text = base64.b64decode(data['data']).decode('utf-8')

        # convert the text to json
        message_data = None
        if body_text:
            message_data = json.loads(body_text)

        return message_data

    def notify_pubsub(self, project, topic, bodystring):
        """Send a PubSub notifiction to a specific project/topic."""
        # format the message data
        data = (f'{bodystring}').encode()

        # create publisher
        publisher = pubsub_v1.PublisherClient()

        # create topic path
        topic_path = publisher.topic_path(project, topic)

        # create a future to publish the message
        future = publisher.publish(topic_path, data=data)

        # log the message
        print(f'Published to {topic} as message {future.result()}'
        )
