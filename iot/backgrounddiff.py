import cv2


fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()


def getdiff(cvimage):
    frame = cv2.cvtColor(cvimage, cv2.COLOR_BGR2GRAY)
    return fgbg.apply(frame)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (5, 5), 2)

        # Do
        frame = getdiff(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
