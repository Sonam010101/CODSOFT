import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        img = Image.open(imagePath).convert("L")
        img_np = np.array(img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])

        faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(img_np)

        for (x,y,w,h) in faces:
            faceSamples.append(img_np[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

os.makedirs("trainer", exist_ok=True)
recognizer.write("trainer/trainer.yml")

print("Training completed successfully!")
