import config
from google.cloud import automl

project = config.project_id
display_name = "cats_ds"

client = automl.AutoMlClient()

project_location = f"projects/{project}/locations/us-central1"

metadata = automl.ImageClassificationDatasetMetadata(classification_type=automl.ClassificationType.MULTICLASS)

dataset = automl.Dataset(
    display_name=display_name,
    image_classification_dataset_metadata=metadata,
)

response = client.create_dataset(parent=project_location, dataset=dataset)

created_dataset = response.result()

print("Dataset name: {}".format(created_dataset.name))
print("Dataset id:{}".format(created_dataset.name.split("/")[-1]))