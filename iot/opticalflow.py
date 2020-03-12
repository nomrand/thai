import cv2

# Shi-Tomasi Parameter
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)
# Lucas-Kanade Parameter
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(
                     cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                     10, 0.03))

gray_prev = None
feature_prev = None


def flow(cvimage):
    global gray_prev, feature_prev
    gray_next = cv2.cvtColor(cvimage, cv2.COLOR_BGR2GRAY)

    if feature_prev is None or len(feature_prev) == 0:
        gray_prev = gray_next
        feature_prev = cv2.goodFeaturesToTrack(
            gray_prev, mask=None, **feature_params)
        return cvimage, None

    # Optical Flow
    feature_next, status, err = cv2.calcOpticalFlowPyrLK(
        gray_prev, gray_next, feature_prev, None, **lk_params)

    # 0:Not Detected, 1:Detected
    good_prev = feature_prev[status == 1]
    good_next = feature_next[status == 1]

    # Result points
    for i, (next_point, prev_point) in enumerate(zip(good_next, good_prev)):
        prev_x, prev_y = prev_point.ravel()
        next_x, next_y = next_point.ravel()
        cvimage = cv2.line(cvimage, (next_x, next_y),
                           (prev_x, prev_y), (0, 0, 255), 2)
        cvimage = cv2.circle(cvimage, (next_x, next_y), 5, (0, 0, 255), -1)

    # Set Next
    gray_prev = gray_next.copy()
    feature_prev = feature_next.reshape(-1, 1, 2)
    return cvimage, good_next


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Do
        frame, points = flow(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
