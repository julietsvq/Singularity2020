import config
from google.cloud import automl

project_id = config.project_id
dataset_id = config.dataset_id
path = config.dataset_csv_path

client = automl.AutoMlClient()

dataset_full_id = client.dataset_path(project_id, "us-central1", dataset_id)

input_uris = path.split(",")
gcs_source = automl.GcsSource(input_uris=input_uris)
input_config = automl.InputConfig(gcs_source=gcs_source)

response = client.import_data(name=dataset_full_id, input_config=input_config)

print("Processing import...")
print("Data imported. {}".format(response.result()))