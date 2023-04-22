import cv2 
import cvlib as cv
from cvlib.object_detection import draw_bbox

# create a video capture object to open the camera and capture live video
video = cv2.VideoCapture(0)

# create an empty list to store detected object labels
labels = []

while True:
    ret, frame = video.read() # read a frame from the video capture object

    # detect common objects in the frame
    # bbox contains the bounding box coordinates of the detected objects
    # label contains the class labels or names of the detected objects
    # conf contains the confidence levels of the detected objects
    bbox, label, conf = cv.detect_common_objects(frame)

    # draw boxes around the detected objects on the frame
    output_image = draw_bbox(frame, bbox, label, conf)

    # display the processed frame in a window titled "Object Detection"
    cv2.imshow("Object Detection", output_image)

    # update the list of detected object labels without duplication
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    # break the loop and close the camera window when the spacebar is pressed
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

i = 0
new_sentence = []

# loop through the detected object labels and creates a sentence to be shown
for label in labels:
    if i == 0:
        new_sentence.append(f"I detected a {label}, and, ")
    else:
        new_sentence.append(f"a {label}")
    i += 1

# print the sentence by joining the words in the new_sentence list
print(" ".join(new_sentence))
