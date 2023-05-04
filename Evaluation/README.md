## Evaluation

This folder containes the codes to the evaluation metrics for Face clustering (in Clustering_Evaluation) and Voice Generation (in TTS_Evaluation)

## Clustering Evaluation

This contains 3 folders corresponding to our 3 clustering algorithms - KMeans, Agglomerative and DBSCAN. Each of the 3 methods are evaluated based on 3 metrics - Silhouette Score, Calinski harabasz Score (C-H Index), and Davies bouldin Score (DB Index). The steps to carry evaluation for each of the 3 approaches is as given below.

#### KMeans

evaluating_kmeans contains the code to evaluate KMeans using the 3 metrics for k (no. of clusters) values ranging from 9 to 99 in intervals of 10.

Steps to run:

* cd into evaluating_kmeans
* run ````python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection_method "cnn"```` to get encodings
* run ````python3 cluster_faces.py --encodings encodings.pickle --jobs -1```` to get evaluation, jobs parameter optional

#### Agglomerative Clustering

#### DBSCAN