import config
from google.cloud import automl

project_id = config.project_id
model_id = config.model_id
file_path = "/Users/jmoreiro/Documents/Events/Datasets/test others/00001224_017.jpg"

prediction_client = automl.PredictionServiceClient()

model_full_id = automl.AutoMlClient.model_path(
    project_id, "us-central1", model_id
)

with open(file_path, "rb") as content_file:
    content = content_file.read()

image = automl.Image(image_bytes=content)
payload = automl.ExamplePayload(image=image)

params = {"score_threshold": "0.8"}

request = automl.PredictRequest(
    name=model_full_id,
    payload=payload,
    params=params
)
response = prediction_client.predict(request=request)

print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))