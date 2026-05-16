from ultralytics import YOLO
import cv2
import pyttsx3
import time

model = YOLO("best.pt")



#last_spoken = ""

frame_count = 0

class_names = ["keys", "remote", "wallet"]

cap = cv2.VideoCapture(0)


current_object = None
last_detected = None


while True:
    print("Current obj",current_object)
    print("Last detected",last_detected)
    print("------")
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count < 5:
        continue

    results = model(frame)

    best_conf = 0

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            # Track highest confidence object
            if conf > best_conf:
                best_conf = conf
                current_object = class_names[cls]
            

            # Draw box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, class_names[cls], (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    # Speak only when object changes
    if current_object != last_detected:
        print(f"Detected: {current_object}")
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(f"{current_object} detected")
        engine.runAndWait()
        time.sleep(0.2)
        del engine
        #last_spoken = current_object

    # # Reset when nothing detected
    # if current_object is None:
    #     last_spoken = ""
    last_detected = current_object

    cv2.imshow("Object Finder", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

