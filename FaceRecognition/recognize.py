import cv2
import os
import time
from progress.bar import ShadyBar as Bar
import sys


def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    # Converting image to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    id = 0
    chk = 0
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        # Predicting the id of the user
        id, chk = clf.predict(gray_img[y:y+h, x:x+w])
        print(id, chk)
        # Check for id of user and label the rectangle accordingly
        if id == 1 and chk < 40:
            cv2.putText(img, "Siva", (x, y-4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        else:
            cv2.putText(img, "Unknown", (x, y-4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]

    return coords, id, chk

# Method to recognize the person


def recognize(img, clf, faceCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255),
             "green": (0, 255, 0), "white": (255, 255, 255)}
    coords, id, chk = draw_boundary(
        img, faceCascade, 1.1, 10, color["white"], "Face", clf)
    return img, id, chk


# Loading classifier
faceCascade = cv2.CascadeClassifier(
    'FaceRecognition/haarcascade_frontalface_default.xml')

# Loading custom classifier to recognize


clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("FaceRecognition/classifier.yml")

# Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
video_capture = cv2.VideoCapture(0)
sys.stdout.flush()
bar = Bar('Recognizing..', max=10)

print('\n')


def Face_Recognizer_Friday():
    f = 0
    n = 0
    while True:
        # Reading image from video stream
        _, img = video_capture.read()
        # Call method we defined above
        img, id, chk = recognize(img, clf, faceCascade)
        # Writing processed image in a new window
        cv2.imshow("face detection", img)

        if id == 1 and chk < 40:
            bar.next()
            f += 1
        else:
            bar.next()
            # print('\r',end='')
            n += 1
        if n == 20:
            # print("unknown")
            video_capture.release()
            # Destroying output window
            cv2.destroyAllWindows()
            bar.finish()
            return False
        if f == 2:
            # print("WelCome Boss")
            # releasing web-cam
            video_capture.release()
            # Destroying output window
            cv2.destroyAllWindows()
            bar.finish()
            return True
        sys.stdout.flush()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False


# Face_Recognizer_Friday()
