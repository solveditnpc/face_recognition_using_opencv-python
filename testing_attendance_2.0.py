import unittest
import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime
import face_recognition
from pathlib import Path

class TestAttendanceSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment before all tests"""
        cls.test_image_dir = "test_images"
        cls.test_csv = "test_attendance.csv"
        os.makedirs(cls.test_image_dir, exist_ok=True)
        
    def setUp(self):
        """Set up before each test"""
        # Create a test image for face detection
        self.test_image = np.zeros((300, 300, 3), dtype=np.uint8)
        cv2.circle(self.test_image, (150, 150), 50, (255, 255, 255), -1)
        self.test_image_path = os.path.join(self.test_image_dir, "test_face.jpg")
        cv2.imwrite(self.test_image_path, self.test_image)
        
    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment after all tests"""
        if os.path.exists(cls.test_image_dir):
            import shutil
            shutil.rmtree(cls.test_image_dir)
        if os.path.exists(cls.test_csv):
            os.remove(cls.test_csv)

    def test_face_detection(self):
        """Test face detection functionality"""
        # Load test image
        image = face_recognition.load_image_file(self.test_image_path)
        
        # Detect faces
        face_locations = face_recognition.face_locations(image)
        
        self.assertGreater(len(face_locations), 0, "Face detection failed")

    def test_face_encoding(self):
        """Test face encoding generation"""
        # Load test image
        image = face_recognition.load_image_file(self.test_image_path)
        
        # Get face encodings
        face_encodings = face_recognition.face_encodings(image)
        
        self.assertGreater(len(face_encodings), 0, "Face encoding generation failed")
        self.assertEqual(len(face_encodings[0]), 128, "Face encoding should be 128-dimensional")

    def test_csv_operations(self):
        """Test CSV file operations"""
        # Create test attendance data
        test_data = {
            'Name': ['Test User'],
            'Time': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        }
        df = pd.DataFrame(test_data)
        
        # Save to CSV
        df.to_csv(self.test_csv, index=False)
        
        # Read and verify
        read_df = pd.read_csv(self.test_csv)
        self.assertEqual(len(read_df), 1, "CSV should contain one record")
        self.assertEqual(read_df['Name'][0], 'Test User', "CSV should contain correct name")

    def test_image_preprocessing(self):
        """Test image preprocessing"""
        # Test image conversion to RGB
        image = cv2.imread(self.test_image_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.assertEqual(len(rgb_image.shape), 3, "Image should be 3-dimensional")
        self.assertEqual(rgb_image.shape[2], 3, "Image should have 3 color channels")

if __name__ == '__main__':
    unittest.main(verbosity=2)
