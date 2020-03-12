import cv2
# https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}

tracker = None


def track(frame, tracker_name=None, initBB=None):
    global tracker
    # check to see if we are currently tracking an object
    if tracker_name is not None:
        tracker = OPENCV_OBJECT_TRACKERS[tracker_name]()
        # start OpenCV object tracker using the supplied bounding box
        tracker.init(frame, initBB)

    # grab the new bounding box coordinates of the object
    (success, box) = tracker.update(frame)
    return (success, box)


if __name__ == '__main__':
    # Capture frame-by-frame
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # select the bounding box of the object we want to track (make
    # sure you press ENTER or SPACE after selecting the ROI)
    initBB = cv2.selectROI("Frame", frame, fromCenter=False,
                           showCrosshair=True)
    print(initBB)

    # Init
    success, box = track(frame, "csrt", initBB)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Do
        success, box = track(frame)

        # Display the resulting frame
        print(success)
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
