## Clustering

This folder contains 3 subfolders for the codes to the clustering algorithms - KMeans, Agglomerative and DBSCAN. The codes include preprocessing of facial images, finding the encodings of the facial images, fitting the clustering model, and storing the clustered images results. The steps to carry out the clustering for each of the 3 approaches is as given below.

#### KMeans

clustering_kmeans contains the code to carry out KMeans clustering.

Steps to run:

* Upload the dataset to drive/local content of Google Colab
* Run the KMeans_Clustering.ipynb file

#### Agglomerative Clustering

clustering_agglomerative contains the code to carry out Agglomerative clustering.

Steps to run:

* Upload the dataset to drive/local content of Google Colab
* Run the Agglomerative_Clustering.ipynb file

#### DBSCAN

clustering_dbscan contains the code to carry out Agglomerative clustering.

Steps to run:

* cd into evaluating_dbscan
* run ````python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection_method "cnn"```` to get encodings, where --dataset specifies path to dataset
* run ````python3 cluster_faces.py --encodings encodings.pickle --jobs -1```` to get evaluation, jobs parameter optional

## TTS Evaluation

