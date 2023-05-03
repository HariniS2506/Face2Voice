# Inference Pipeline

For a given facial test image, the code calculates the Euclidean distance of the embeddings of the test face from the centroid of every cluster and chooses the closest cluster. The fine tuned TTS model is then read and the resultant voice is generated.

# Data structure

The folder must be of the following structure:

Final_Clusters
|
|---0
    |--centroid.npy
    |--best_model.pth
    |--config.json
|---1
    |--centroid.npy
    |--best_model.pth
    |--config.json 
.
.
.
.

