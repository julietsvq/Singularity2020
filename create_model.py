import config
from google.cloud import automl

project_id = config.project_id
dataset_id = config.dataset_id
display_name = "catsML"

client = automl.AutoMlClient()

project_location = f"projects/{project_id}/locations/us-central1"

metadata = automl.ImageClassificationModelMetadata(
    train_budget_milli_node_hours=24000
)
model = automl.Model(
    display_name=display_name,
    dataset_id=dataset_id,
    image_classification_model_metadata=metadata,
)

response = client.create_model(parent=project_location, model=model)

print("Training operation name: {}".format(response.operation.name))
print("Training started...")

model_id = response.result().name.split("/")[-1]
print ("Model ID: " + model_id)

model_full_id = client.model_path(project_id, "us-central1", model_id)
response = client.deploy_model(name=model_full_id)

print("Model deployment finished: {}".format(response.result()))


