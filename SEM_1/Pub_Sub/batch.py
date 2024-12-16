from google.cloud.bigquery.schema import Schema

def load_tsv_to_bigquery(
    tsv_file_path: str,
    table_id: str,
    project_id: str,
    dataset_id: str,
    schema: bigquery.Schema
):
    """Loads data from a local TSV file into a BigQuery table.

    Args:
        tsv_file_path: Path to the local TSV file.
        table_id: ID of the destination BigQuery table.
        project_id: ID of the Google Cloud project.
        dataset_id: ID of the BigQuery dataset.
        schema: The schema definition for the BigQuery table.
    """

    client = bigquery.Client(project=project_id)
    table_ref = client.dataset(dataset_id).table(table_id)

    try:
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            field_delimiter="\t",
            schema=schema
        )

        with open(tsv_file_path, "rb") as source_file:
            job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
            job.result()  # Wait for the job to complete

        print(f"Loaded data from {tsv_file_path} into {project_id}.{dataset_id}.{table_id}")
    except Exception as e:
        print(f"Error loading data: {e}")

# Define the schema based on your TSV file
schema = [
    bigquery.SchemaField("match_id", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("season", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("start_date", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("venue", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("innings", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("ball", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("batting_team", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("bowling_team", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("striker", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("non_striker", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("bowler", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("runs_off_bat", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("extras", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("wides", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("noballs", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("byes", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("legbyes", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("penalty", bigquery.SchemaField.Type.INTEGER),
    bigquery.SchemaField("wicket_type", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("player_dismissed", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("other_wicket_type", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("other_player_dismissed", bigquery.SchemaField.Type.STRING),
    bigquery.SchemaField("cricsheet_id", bigquery.SchemaField.Type.INTEGER)
]

# Example usage
tsv_file_path = "D:\\BDA_Sem_1\\manipal-workshop\\data.tsv"
table_id = "Ipl"
project_id = "projectpubsub-436211"
dataset_id = "iplbukcet"

load_tsv_to_bigquery(tsv_file_path, table_id, project_id, dataset_id, schema)