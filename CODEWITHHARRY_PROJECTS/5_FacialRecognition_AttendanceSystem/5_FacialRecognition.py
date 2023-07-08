import face_recognition_models
import cv2
import numpy as np
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0)

# Load Known faces
nayans_image = face_recognition_models.load_image_file("faces/nayan.jpg")
nayan_encoding = face_recognition_models.
papas_image = face_recognition_models.load_image_file("faces/papa.jpg")

import face_recognition_models
img = face_recognition_models.load_image_file("faces/img.jpg")
face_locations = face_recognition_models.face_locations(img)
