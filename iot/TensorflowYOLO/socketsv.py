import time
import socketcon
import detect
import yolodetect
import cv2


detector = detect.Detector(0.5, 0.5)


def callback(byte):
    frame = cv2.imdecode(byte, flags=cv2.IMREAD_COLOR)

    start = time.time()
    frame = cv2.resize(frame, dsize=(416, 416),
                       interpolation=cv2.INTER_NEAREST)
    result = detector.detect(frame)
    print("***TIME:", time.time()-start)
    result = yolodetect.result_ordered(result)
    return result


if __name__ == "__main__":
    socketcon.server(callback)
    detector.close()
