# Singularity2020

Here you can find the slides for the [Singularity Tech Day 2020](https://singularitytechday.com) session [Cloud AutoML](https://github.com/julietsvq/Singularity2020/blob/main/Cloud%20AutoML%20Singularity%20TechDay%202020%20Repo.pdf) and demo. The goal of this demo is to classify images of cats so that it can detect when the image is of your own cat, or when the image is of other cats. This can be done either using the graphical interface of the AutoML Vision console in Google Cloud, as shown during the presentation, or via code following the steps below.

Check prerequisites and other general information on how to create datasets and train your models at: 

[AutoML Vision API Tutorial](https://cloud.google.com/vision/automl/docs/tutorial#tutorial-translate-evaluate-python)

Create a storage bucket to store the images you will use for training your model, for this demo select Region / us-central1. You can create your bucket from the [GCP console](https://cloud.google.com/storage/docs/quickstart-console) or using the [gstutil mb command](https://cloud.google.com/storage/docs/gsutil/commands/mb)

Now upload your images to your storage bucket. For this you can click [Upload Files in the console](https://cloud.google.com/storage/docs/quickstart-console#upload_an_object_into_the_bucket) or use the [gsutil cp command](https://cloud.google.com/storage/docs/gsutil/commands/cp).
For this demo, you can use the images of cats from [this dataset](https://www.kaggle.com/crawford/cat-dataset) and add the images of your cat. The way in which I have organized these images by folders in my storage bucket so that in the next step we can create a csv file listing all the images with its corresponding label is this: 

mycat/ - images of the cat I want to detect

other/ - images of other cats taken from the previously linked dataset

Next run the code to generate the csv file, create the dataset and import your images to it, train and evaluate your model, and finally make predictions using your model. After each of these steps, you can check your Google Cloud Vision AutoML console to see how the dataset is created, your model trained, etc: 


[generate_csv.py](https://github.com/julietsvq/Singularity2020/blob/main/generate_csv.py) - This will create a csv file called cats.csv and store it in your bucket, listing all the images with its path in the storage bucket and adding a label to each, corresponding to the name of the folder they are in (in this case, two labels: mycat and other).

[create_dataset.py](https://github.com/julietsvq/Singularity2020/blob/main/create_dataset.py) - This will create a new empty dataset called cats_ds.

[import_dataset.py](https://github.com/julietsvq/Singularity2020/blob/main/import_dataset.py) - This will import the images listed in our csv file into our newly created dataset.

[create_model.py](https://github.com/julietsvq/Singularity2020/blob/main/create_model.py) - Here we will create and train our model.

[evaluate_model.py](https://github.com/julietsvq/Singularity2020/blob/main/evaluate_model.py) - It will print our model’s evaluation metrics.

[predict.py](https://github.com/julietsvq/Singularity2020/blob/main/predict.py) - Use this to make prediction calls for your new images.

 

