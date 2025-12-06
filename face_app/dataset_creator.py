import cv2
import os

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

user_id = input("Enter User ID (number): ")

count = 0

os.makedirs("dataset", exist_ok=True)

print("Capturing 50 images. Press q to quit early.")

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1

        cv2.imwrite(f"dataset/User.{user_id}.{count}.jpg", gray[y:y+h, x:x+w])

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif count >= 50:
        break

cam.release()
cv2.destroyAllWindows()

print("Dataset created successfully!")
