from ultralytics import YOLO
import cv2
import pyttsx3
import time
import threading


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()


model = YOLO("yolov8n.pt")   

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)


target_objects = [
    "person",
    "car",
    "bus",
    "truck",
    "bicycle",
    "motorcycle",
    "chair",
    "bench"
]

CONFIDENCE = 0.5
cooldown = 4
last_time = 0


print("Smart VisionGuide Started")
print("ESC to exit")

def get_direction(x1, x2, width):

    center = (x1 + x2) / 2

    if center < width / 3:
        return "left"

    elif center > 2 * width / 3:
        return "right"

    else:
        return "ahead"


def get_distance(box_width):

    if box_width > 250:
        return "very close"

    elif box_width > 120:
        return "close"

    else:
        return "far"

while True:

    ret, frame = cap.read()

    if not ret:
        break

    h, w, _ = frame.shape

    results = model(frame, verbose=False)

    detected_messages = []

    current_time = time.time()


    for r in results:

        for box in r.boxes:

            conf = float(box.conf[0])

            if conf < CONFIDENCE:
                continue

            cls = int(box.cls[0])
            label = model.names[cls]

            if label not in target_objects:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            box_width = x2 - x1

            direction = get_direction(x1, x2, w)

            distance = get_distance(box_width)

            message = f"{label} {direction} {distance}"

            detected_messages.append(message)

            # COLOR
            color = (0, 0, 255)


            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            cv2.putText(
                frame,
                message,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )

    if detected_messages and (current_time - last_time > cooldown):

        msg = detected_messages[0]

        print("ALERT:", msg)

        threading.Thread(
            target=speak,
            args=(msg,),
            daemon=True
        ).start()

        last_time = current_time


    cv2.putText(
        frame,
        "VISION GUIDE AI",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
    )

    cv2.imshow("VisionGuide Pro", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()

print("Stopped")

