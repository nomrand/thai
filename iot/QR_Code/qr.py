import cv2


def read(cvimage):
    qrDecoder = cv2.QRCodeDetector()
    # Detect and decode the qrcode
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(cvimage)
    if len(data) > 0:
        # Success
        return data
    return None


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        result = read(frame)
        if result is not None:
            print(result)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
