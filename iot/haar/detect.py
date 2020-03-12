# https://github.com/opencv/opencv/tree/master/data/haarcascades
import os
import cv2

XMLS = {
    "face": "haarcascade_frontalface_default.xml",
    "cat": "haarcascade_frontalcatface.xml",
    "smile": "haarcascade_smile.xml",
}


SCALE_FACTOR = 1.15
MIN_NEIGHBOR = 3


def detect(cvimage, classifier):
    cascade = cv2.CascadeClassifier(os.path.join(
        os.path.dirname(__file__), XMLS[classifier]))

    return cascade.detectMultiScale(
        cvimage,
        scaleFactor=SCALE_FACTOR,
        minNeighbors=MIN_NEIGHBOR)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Do
        facerects = detect(frame, "cat")
        for rect in facerects:
            cv2.rectangle(
                frame,
                tuple(rect[0:2]),
                tuple(rect[0:2] + rect[2:4]),
                (0, 0, 255),
                thickness=2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
