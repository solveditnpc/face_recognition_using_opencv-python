"""
MIT License

Copyright (c) 2025 solveditnpc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Generalised the code for import of names and face_encodings 
# Unknown faces are now saved in a folder named unknown_faces in the project directory
# Fixed the issue where time of the recognition was same for all the faces recognised 
# Follow the dictionary format in store1.csv ie "name" "image_path" if you import your own file 
import cv2
import csv
import face_recognition
import numpy as np
import datetime
import os

# Create a folder for unknown faces if it doesn't exist already
unknown_faces_folder = "unknown_faces" 
os.makedirs(unknown_faces_folder, exist_ok=True)

video_capture = cv2.VideoCapture(0)

# Specify the folder location and csv file location
database_folder = "paste your database path or the file name if it exists in this projects directory"
csv_file = "paste your csv file path or the file name if it exists in this projects directory"

# Store the faceencodings and names of the people in the database
known_face_encodings = []
known_face_names = []

# Read the CSV file and load face encodings
with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        image_path = os.path.join(database_folder, row['image_path'])
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(row['name'])

# Creating a copy of the names list
students = known_face_names.copy()

# Get the current date for the CSV filename
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Open the CSV file for writing, or create it 
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Initialize a counter for unknown faces
unknown_face_counter = 1

#Check if the unknown faces in the webcam feed are already in the unknown folder  
def is_face_unique(face_encoding, folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            saved_image = face_recognition.load_image_file(os.path.join(folder_path, filename))
            saved_face_encodings = face_recognition.face_encodings(saved_image)
            if saved_face_encodings:
                saved_face_encoding = saved_face_encodings[0]
                matches = face_recognition.compare_faces([saved_face_encoding], face_encoding)
                if matches[0]:
                    return False
    return True

# Explained in the last version
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        
        name = "Unknown"

        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
         
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        if name == "Unknown":
            # Add the unknown faces not already in the unknown folder to the unknown folder 
            if is_face_unique(face_encoding, unknown_faces_folder):
                face_image = frame[top:bottom, left:right]
                face_filename = f"{unknown_faces_folder}/unknown{unknown_face_counter}.jpg"
                cv2.imwrite(face_filename, face_image)
                unknown_face_counter += 1

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.6, (255, 255, 255), 1)

        if name in students:
            students.remove(name)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            lnwriter.writerow([name, current_time])

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()