import time
import cv2
import detect


TARGET = {
    # "person": 0,
    "cat": 15,
    "dog": 16,
}


def result_ordered(result, target=TARGET):
    detects = []
    res_map = result[0]
    if len(res_map) > 0:
        for targettype in target:
            res_target = res_map[target[targettype]]
            if len(res_target) > 0:
                for res_one in res_target:
                    detects.append({
                        "type": targettype,
                        "rect": [int(x) for x in res_one[:4]],
                        "accuracy": float(res_one[4]),
                    })
        detects.sort(key=lambda o: o["accuracy"], reverse=True)

    return detects


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    detector = detect.Detector(0.5, 0.5)

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, dsize=(416, 416),
                           interpolation=cv2.INTER_NEAREST)

        # Detect
        start = time.time()
        result = detector.detect(frame)
        print("***TIME:", time.time()-start)

        # Show Result
        res_ordered = result_ordered(result, {
            "person": 0,
            "cat": 15,
            "dog": 16,
        })
        for d in res_ordered:
            print(d)
            cv2.rectangle(frame,
                          tuple(d["rect"][:2]),
                          tuple(d["rect"][2:4]),
                          (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            detector.close()
            break
