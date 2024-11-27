from google.cloud import bigquery
from google.cloud import pubsub_v1
import functions_framework
import json
import base64
from cloudevents.http import CloudEvent

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def load_pubsub_to_bigquery(event):
    """
    Reads a JSON-formatted message from Pub/Sub and inserts it into a BigQuery table.

    Args:
        event (dict): Event payload.
            event['data']: The data published to the Pub/Sub topic, as a base64-encoded string.
    """
    # Decode the Pub/Sub message data
    message = base64.b64decode(event.data["message"]["data"]).decode()

    # Parse the JSON message
    try:
        data = json.loads(message)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return  # Exit if JSON decoding fails

    # Set your BigQuery project ID and dataset/table IDs
    project_id = "bubbly-benefit-426415-h5"
    dataset_id = "datalake"
    table_id = "ipl_raw"

    # Create a BigQuery client
    client = bigquery.Client(project=project_id)

    # Get a reference to the BigQuery table
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    # Insert the data into the BigQuery table
    errors = client.insert_rows(table, [data])  # Data must be a list of rows

    # Check for errors
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")
    else:
        print(f"Data successfully inserted into BigQuery table {project_id}.{dataset_id}.{table_id}")

