# ai-tracking
Sofwerx automated intrusion tracking repository

###In order for the person_detection.py script to work, a few things need to be checked.
1. python 2.7 installed
2. tensorflow installed/built
3. opencv installed/build
4. numpy installed
5. pandas installed
6. other dependencies at the top, to be imported, installed

7. Make sure you have the tensorflow models installed and protoc'd, such that you have the directory /tensorflow/models/research/object_detection/
essentially, cd / and then git clone https://github.com/tensorflow/models.git
8. the person_detection.py script is in that directory

9. https://github.com/sofwerx/assault-rifle-detection do this, but instead of the longgun_detection.py, use the person_detection.py
10. Inside the tf_files folder, create two folders: save_image and save_threat image
then, you should be able to run the script


how to run:
  `python switch_n_type.py forw 0.5`
    ### the number is the time in seconds, first arg can be either forw or back
