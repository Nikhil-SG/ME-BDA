from google.cloud import bigquery

def load_tsv_to_bigquery(
    tsv_file_path: str, 
    table_id: str, 
    project_id: str, 
    dataset_id: str
) -> None:
    """Loads data from a local TSV file into a BigQuery table.

    Args:
        tsv_file_path: Path to the local TSV file.
        table_id: ID of the destination BigQuery table.
        project_id: ID of the Google Cloud project.
        dataset_id: ID of the BigQuery dataset.
    """

    client = bigquery.Client(project=project_id)
    table_ref = client.dataset(dataset_id).table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        field_delimiter="\t",
    )

    with open(tsv_file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        job.result()  # Wait for the job to complete

    print(f"Loaded data from {tsv_file_path} into {project_id}.{dataset_id}.{table_id}")

# Example usage:
tsv_file_path = "data.tsv"
table_id = "batch_ipl"
project_id = "bubbly-benefit-426415-h5"
dataset_id = "chiru_ipl"

load_tsv_to_bigquery(tsv_file_path, table_id, project_id, dataset_id)
