import os
import config
from google.cloud import storage

storage_client = storage.Client()

bucket_name = config.bucket
paths_in_bucket = config.paths

filename = 'cats.csv'

with open(filename, 'w+') as f:
    for path in paths_in_bucket:
        blobs = storage_client.list_blobs(bucket_name, prefix=path)
        for blob in blobs:
            if '.jpg' in blob.name:
                bucket_path = 'gs://' + os.path.join(bucket_name, blob.name)
                label = blob.name.split('/')[-2]
                f.write(', '.join([bucket_path, label]))
                f.write("\n")

bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(filename)
blob.upload_from_filename(filename)

csv_uri = 'gs://' + os.path.join(bucket_name, blob.name)
print("Dataset csv path: {}".format(csv_uri))