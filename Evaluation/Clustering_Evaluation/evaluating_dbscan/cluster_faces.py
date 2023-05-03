# USAGE
# python3 cluster_faces.py --encodings encodings.pickle --jobs -1

# import the necessary packages
# DBSCAN model for clustering similar encodings
from sklearn.cluster import DBSCAN
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
clt = DBSCAN(eps=0.4, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.4): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.4) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.4) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.41, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.41): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.41) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.41) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.42, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.42): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.42) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.42) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.43, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.43): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.43) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.43) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.44, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.44): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.44) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.44) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.45, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.45): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.45) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.45) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.46, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.46): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.46) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.46) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.47, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.47): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.47) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.47) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.48, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.48): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.48) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.48) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better

# creating DBSCAN object for clustering the encodings with the metric "euclidean"
clt = DBSCAN(eps=0.49, metric="euclidean", n_jobs=args["jobs"]) #can tweak eps
clt.fit(encodings)

print(f'Silhouette Score(eps=0.49): {silhouette_score(encodings, clt.labels_)}') #-1, 0-1 bad-good
print(f'Calinski harabasz Score(eps=0.49) C-H Index: {calinski_harabasz_score(encodings, clt.labels_)}') #higher the better
print(f'Davies bouldin Score(eps=0.49) DB Index: {davies_bouldin_score(encodings, clt.labels_)}') #lower the better