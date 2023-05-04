## Fine Tuning TTS Models

* For each cluster we fine tuned a TTS Model.
* You can fine-tune a model by running the cells in Whisper_STT_and_Coqui_TTS.ipynb sequentially.
* The data for the fine-tuning is stored at https://drive.google.com/drive/folders/1-5qJ6DViLN_PHl93pZ9mq8J640RYIvfk?usp=sharing
* The structure of the data folder is as follows:
  Final_data
     | Cluster_faces
     | Cluster_voices
          |0
            |id_1
               |sub_folder
                  |*.wav
               |sub_folder
                  |*.wav
               ...
            |id_2
            |id_3
          |1
          |3
          |4
          ....
          
* Within each cluster, there is a separate folder for each person in the cluster. And within each of those folders, there are multiple subfolders and the wav files are in those subfolders. So we first run a script to extract all the wav files from all subfolders and place them in one parent folder(voices_{cluster_no.}. For example, all wav files in cluster 0 are placed in voices_0. We do this for all clusters.
* To run the fine tuning notebook:
   - Based on the cluster that you are fine-tuning for, set $upload_dir and $output_directory.
* We have done some further processing of the wav files after this. Run the cells sequentially. The wav files after processing are stored in the $dataset_dir which is inside the ````voices_{sub_dir}```` folder.
* We then use Hugging Face's implememtation of Whisper to create transcripts for all the wav files and store them in one file: metadata.csv.
* TTS requires such a file.
* We then download the base model and run the fine tuning script.
* The fine-tuned model gets saved in the $output_directory in ````voices_{sub_fir}````.
* We can now use this fine tuned model and a text input to generate a was file.


