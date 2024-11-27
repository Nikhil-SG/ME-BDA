import csv
import json
from google.cloud import pubsub_v1
import pandas as pd

def publish_message(project_id, topic_id, message):
    """Publishes a message to a Google Cloud Pub/Sub topic.

    Args:
        project_id: The ID of the Google Cloud project containing the topic.
        topic_id: The ID of the Pub/Sub topic to publish to.
        message: The message to publish.

    Returns:
        The message ID of the published message.
    """

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    # Data must be a bytestring
    data = message.encode("utf-8")
    future = publisher.publish(topic_path, data)
    message_id = future.result()

    print(f"Published message with ID {message_id} to topic {topic_path}.")
    return message_id

# Example usage:


def csv_to_json(tsv_file_path):
    """Reads data from a CSV file and converts it to JSON format.

    Args:
        csv_file_path: The path to the CSV file.

    Returns:
        A list of dictionaries representing the CSV data in JSON format.
    """
    df = pd.read_csv(tsv_file_path, delimiter="\t")
    df.fillna('', inplace=True)
    return df

def main():
    df = csv_to_json('data.tsv')
    data_dict = df.to_dict(orient='records')
    for record in data_dict:
        json_data = json.dumps(record)
        publish_message("bubbly-benefit-426415-h5", "chiru-demo", json_data)
        print(json_data)
        break

main()
