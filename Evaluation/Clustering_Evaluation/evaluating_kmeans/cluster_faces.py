# USAGE
# python3 cluster_faces.py --encodings encodings.pickle --jobs -1

# import the necessary packages
# DBSCAN model for clustering similar encodings
from sklearn.cluster import KMeans
from imutils import build_montages
import numpy as np
import argparse
import pickle
import cv2
import shutil
import os
from constants import ENCODINGS_PATH, CLUSTERING_RESULT_PATH
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-j", "--jobs", type=int, default=-1,
	help="# of parallel jobs to run (-1 will use all CPUs)")
args = vars(ap.parse_args())

# load the serialized face encodings + bounding box locations from
# disk/encodings pickle file, then extract the set of encodings to so we can cluster on them

print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())
data = np.array(data)
encodings = [d["encoding"] for d in data] # list of encodings
print("lennn", len(encodings))

# cluster the embeddings
print("[INFO] clustering...")

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
kmeans = KMeans(n_clusters=9, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=9): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=9) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=9) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=19, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=19): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=19) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=19) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=29, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=29): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=29) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=29) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=39, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=39): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=39) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=39) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=49, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=49): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=49) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=49) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=59, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=59): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=59) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=59) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=69, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=69): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=69) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=69) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=79, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=79): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=79) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=79) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=89, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=89): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=89) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=89) DB Index: {davies_bouldin_score(encodings, labs)}') #lower

kmeans = KMeans(n_clusters=99, random_state=22)
kmeans.fit(encodings)

labs=kmeans.predict(encodings)

print(f'KMeans Silhouette Score(n=99): {silhouette_score(encodings, labs)}') #-1, 0-1 bad-good
print(f'KMeans Calinski harabasz Score(n=99) C-H Index: {calinski_harabasz_score(encodings, labs)}') #higher the better
print(f'KMeans Davies bouldin Score(n=99) DB Index: {davies_bouldin_score(encodings, labs)}') #lower
