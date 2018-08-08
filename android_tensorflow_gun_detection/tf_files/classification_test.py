# import packages
import tensorflow as tf, sys
import os, glob
from IPython.display import Image, display
import cv2

cap = cv2.VideoCapture(0)

# Get training labels
label_lines=[line.rstrip() for line in tf.gfile.GFile("/tf_files/output/retrained_labels.txt")]

decisionMatrixHeader = []
for label in label_lines:
    decisionMatrixHeader.append(label)

# Import trained inception model
with tf.gfile.FastGFile("/tf_files/output/retrained_graph.pb", 'rb') as f:
    graph_def =  tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def,name='')

with tf.Session() as sess:


    save_image_dir = "/tf_files/test_images/classification/"

    while True:
        ret, frame = cap.read()
        #cv2.imshow(frame)

        ret, image_np = cap.read()
		# Expand dimensions since the model expects images to have shape: [1, None, None, 3]
		image_np_expanded = np.expand_dims(image_np, axis=0)
		image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        predictions = sess.run(image_tensor, {'DecodeJpeg/contents:0':img_str})                                                           
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]   

        decisionArray = []                                              
        for node_id in top_k:                                           
            human_string = label_lines[node_id]                         
            score = predictions[0][node_id]                             
            print('%s (score = %5f)' % (human_string,score))            
            decisionArray.append([score, human_string]) 
        

        # final_decision[0] is the score
        # final_decision[1] is the name
         
        final_decision = max(decisionArray)        
        print file + " contains " + final_decision[1] + '\n'
        decisionMatrix[label_lines.index(final_decision[1])] = decisionMatrix[label_lines.index(final_decision[1])] + 1

        # save copy in classification folder
        os.system('cp %s %s%s_%5f_%s.jpg' % (image_path, save_image_dir, os.path.splitext(file)[0], final_decision[0], final_decision[1]))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break




# with tf.Session() as sess:
    
#     os.chdir("/tf_files/test_images")
#     count1=1
    
#     decisionMatrix = [0, 0]

#     for file in glob.glob("*.jpg"):
    
#         image_path = "/tf_files/test_images" + '/' + file
#         save_image_dir = "/tf_files/test_images/classification/"
        
#         # display(Image(filename=image_path))

#         image_data=tf.gfile.FastGFile(image_path,'rb').read()                                                              
#         softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
#         predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0':image_data})                                                           
#         top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]   

#         decisionArray = []                                              
#         for node_id in top_k:                                           
#             human_string = label_lines[node_id]                         
#             score = predictions[0][node_id]                             
#             print('%s (score = %5f)' % (human_string,score))            
#             decisionArray.append([score, human_string]) 
        

#         # final_decision[0] is the score
#         # final_decision[1] is the name
         
#         final_decision = max(decisionArray)        
#         print file + " contains " + final_decision[1] + '\n'
#         decisionMatrix[label_lines.index(final_decision[1])] = decisionMatrix[label_lines.index(final_decision[1])] + 1

#         # save copy in classification folder
#         os.system('cp %s %s%s_%5f_%s.jpg' % (image_path, save_image_dir, os.path.splitext(file)[0], final_decision[0], final_decision[1]))


    print(decisionMatrixHeader)
    print(decisionMatrix)