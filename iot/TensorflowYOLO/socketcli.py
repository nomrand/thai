import sys
import cv2
import socketcon

DETECT_SIZE = 416
ORG_SIZE = 416


if __name__ == "__main__":
    serverip = sys.argv[1]
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, dsize=(ORG_SIZE, ORG_SIZE),
                           interpolation=cv2.INTER_NEAREST)
        ret, byte = cv2.imencode('.jpg', frame, encode_param)
        if not ret:
            continue

        result = socketcon.client(serverip, byte)
        for detected in result:
            cv2.rectangle(
                frame,
                tuple(int(x * (ORG_SIZE / DETECT_SIZE))
                      for x in detected["rect"][:2]),
                tuple(int(x * (ORG_SIZE / DETECT_SIZE))
                      for x in detected["rect"][2:4]),
                (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
