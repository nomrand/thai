import numpy as np
import cv2


def detect_red(cvimage, minsize):
    hsv = cv2.cvtColor(cvimage, cv2.COLOR_BGR2HSV)

    hsv_min = np.array([0, 100, 0])
    hsv_max = np.array([30, 255, 255])
    range1 = cv2.inRange(hsv, hsv_min, hsv_max)

    hsv_min = np.array([150, 100, 0])
    hsv_max = np.array([179, 255, 255])
    range2 = cv2.inRange(hsv, hsv_min, hsv_max)

    return detect(range1 + range2, minsize, cvimage)


def detect_blue(cvimage, minsize):
    hsv = cv2.cvtColor(cvimage, cv2.COLOR_BGR2HSV)
    hsv_min = np.array([90, 100, 0])
    hsv_max = np.array([130, 255, 255])
    range1 = cv2.inRange(hsv, hsv_min, hsv_max)
    return detect(range1, minsize, cvimage)


def detect_green(cvimage, minsize):
    hsv = cv2.cvtColor(cvimage, cv2.COLOR_BGR2HSV)
    hsv_min = np.array([30, 100, 0])
    hsv_max = np.array([65, 255, 255])
    range1 = cv2.inRange(hsv, hsv_min, hsv_max)
    return detect(range1, minsize, cvimage)


def detect(cvimage, minsize, orgimage):
    # Find
    contours, _ = cv2.findContours(
        cvimage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the edges
    cvimage = cv2.drawContours(
        orgimage, contours, -1, (0, 255, 0), 1)

    # count & draw sub info
    results = []
    for i in range(0, len(contours)):
        # remove small objects
        area = cv2.contourArea(contours[i])
        if area < minsize:
            continue

        # Draw the count of contours
        cv2.putText(
            cvimage,
            str(len(results) + 1),
            (contours[i][0][0][0], contours[i][0][0][1]),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255, 0, 0)
        )

        results.append({"area": area, "pos": contours[i]})

    return cvimage, results


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (5, 5), 2)

        # Do
        result_img, results = detect_red(frame, 500)
        print("detect:" + str(len(results)))

        # Display the resulting frame
        cv2.imshow('frame', result_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
