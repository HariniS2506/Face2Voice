## Inference Pipeline

For a given facial test image, the code calculates the Euclidean distance of the embeddings of the test face from the centroid of every cluster and chooses the closest cluster. The fine tuned TTS model is then read and the resultant voice is generated.

## Data structure

The folder must be of the following structure:

Final_Clusters <br>
| <br>
|---0 <br>
&nbsp; &nbsp; &nbsp;    |--centroid.npy <br>
&nbsp; &nbsp; &nbsp;     |--best_model.pth <br>
&nbsp; &nbsp; &nbsp;     |--config.json <br>
|---1 <br>
&nbsp; &nbsp; &nbsp;     |--centroid.npy <br>
 &nbsp; &nbsp; &nbsp;    |--best_model.pth <br>
 &nbsp; &nbsp; &nbsp;    |--config.json <br>
. <br>
. <br>
. <br>
. <br>

