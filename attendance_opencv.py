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

import face_recognition
import cv2
import numpy as np
import csv 
from datetime import datetime

# 0 is for the inbuilt camera, 1 for first external camera and so on 
video_capture = cv2.VideoCapture(0)          

# Load known faces
# This section can be expanded as per your need ie person1,person2,person3,...,personn
person1_image = face_recognition.load_image_file("D:/person1.jpg")      # Fill the image path instead of person1.jpg
person1_encoding = face_recognition.face_encodings(person1_image)[0]         

person2_image = face_recognition.load_image_file("D:/person2.jpg")
person2_encoding = face_recognition.face_encodings(person2_image)[0]

known_face_encodings = [person1_encoding , person2_encoding]            # You need to add face encoding for each person you add 
known_face_names = ["person1" , "person2"]                              # Instead of person1,2 use the persons name 

# List of expected students 
students = known_face_names.copy()

# Get the current date and time 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open csvfile
f = open(f"{current_date}.csv" , "w+" , newline="")
lnwriter = csv.writer(f)

# Loop to process each frame
while True:
    # read a frame from the captured video
    ret, frame = video_capture.read()
    # convert the frame from BGR format used by opencv to RGB format used by face_recognition
    rgb_frame = frame[:, :, ::-1]
    
    # Find all the faces and face_encodings in the video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
    
    # Loop through each frame of this video
    for(top, right, bottom, left), face_encoding in zip(face_locations,face_encodings):
        # See if the face in the frame is match for known faces
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        
        name = "Unknown"
        
        # Use the first recognised face or use the face with smallest distance to the new face
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a lable below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        # Add text to the frame 
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom -6), font, 0.6, (255, 255, 255), 1)
        
        # If person is already in list then remove from expected list of people, add names to csvfile
        if name in students:
                    students.remove(name)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name,current_time])
    
    # Display the frame with text annotations 
    cv2.imshow('Video', frame)
    # Hit 'q' on keyboard to stop/quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()