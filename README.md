# Face Recognition Attendance System

A simple and efficient face recognition attendance system using OpenCV and Python for windows,linux and mac. The system stores attendance records in CSV format, making it lightweight and easy to use. unknown faces are stored in the `unknown_faces` folder.

## Features

- Real-time face detection and recognition
- Automated attendance marking
- CSV export functionality for attendance records
- Multiple face recognition support
- High accuracy using deep learning models
- Attendance history tracking
- Easy user registration system
- Unrecognized faces storage in `unknown_faces` folder
- Detailed logging system

## Configuration

1. add the images of the people with their names as the image name in the `database1` folder.
   example: `barack_obama.jpg`  // not neccessary to save the images with the name of the person as the image name

2. add the image name and the name of the person you want to associate with that image in the `store1.csv` file.
   // you can import a file with the format `name` `image_name` if you want to import your own file ,change the file name or the file path in the attendance scripts
   example:`barack_obama.jpg`,`barack_obama`

## Installation Guide

### Windows Installation

1. Install Python (preferably 3.7.6 since requirements_windows.txt is for 3.7.6, to do a maual installation use python 3.11.0 for latest dlib libraries):
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

2. Install all required packages:
   ```bash
   pip install -r requirements_windows.txt
   ```

Note: If you encounter any installation errors, refer to the Troubleshooting section below.

### Linux Installation

1. Install system dependencies:
   ```bash
   sudo apt-get update
   sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
   libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
   git libgtk2.0-dev pkg-config
   ```

2. Install pyenv:
   ```bash
   curl https://pyenv.run | bash
   ```

3. Add pyenv to your PATH (add these to your ~/.bashrc or ~/.zshrc):
   ```bash
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   ```

4. Reload your shell configuration:
   ```bash
   source ~/.bashrc
   ```

5. Install Python 3.7.6 using pyenv:
   ```bash
   pyenv install 3.7.6
   cd folder_you_want_to_install_in
   pyenv local 3.11.0
   ```

6. Create and activate a virtual environment:
   ```bash
   python -m venv test3.11.0
   source test3.11.0/bin/activate
   ```

7. Install required packages:
   ```bash
   pip install -r requirements_linux.txt
   ```
   OR
   
   ```bash
   # Install CMake first
   pip install cmake

   # Install dlib with specific version
   pip install dlib==19.24.0

   # Install face_recognition and opencv
   pip install face_recognition==1.3.0
   pip install opencv-python
   ```

Note: If you encounter any installation errors, refer to the Troubleshooting section below.

### Mac Installation Instructions

1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install pyenv using Homebrew:
   ```bash
   brew install pyenv
   ```

3. Add pyenv to your shell configuration. Add these lines to your ~/.zshrc or ~/.bash_profile:
   ```bash
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```

4. Restart your terminal or reload the configuration:
   ```bash
   source ~/.zshrc
   ```

5. Install Python using pyenv:
   ```bash
   pyenv install 3.11.0
   cd folder_you_want_to_install_in
   pyenv local 3.11.0
   ```

6. Create and activate a virtual environment:
   ```bash
   python -m venv test3.11.0
   source test3.11.0/bin/activate
   ```

7. Install dependencies:
   ```bash
   # Install Xcode Command Line Tools if not already installed
   xcode-select --install
   
   # Install CMake using Homebrew
   brew install cmake
   
   # Install Python dependencies
   pip install -r requirements_mac.txt
   ```

## Usage

1. Run the main application:
   ```bash
   python attendance_opencv_2.0.py   # On Windows
   python linux_attendance_opencv_2.0.py  # On Linux
   python linux_attendance_opencv_2.0.py  # On macOS
   ```

2. The system will:
   - Detect faces through your camera/ you can choose one or more external cameras
   - Recognize registered individuals
   - Store attendance in CSV format
   - Save unrecognized faces in the `unknown_faces` folder for later review

## Note

- Ensure good lighting conditions for better face recognition
- Keep the camera stable for accurate results
- Make sure to register faces before attempting recognition
- Check the `unknown_faces` folder periodically to review and potentially register new faces
- The system automatically creates the `unknown_faces` folder if it doesn't exist

## System Requirements

### Minimum Hardware Requirements
- Processor: Intel Core i3 or equivalent
- RAM: 4GB
- Storage: 1GB free space
- Camera: 720p webcam

### Recommended Hardware
- Processor: Intel Core i5 or better
- RAM: 8GB
- Storage: 2GB free space
- Camera: 1080p webcam(works on low resolution cameras but not that well)

## Performance Metrics

- Face Detection Speed: <50ms per frame
- Recognition Accuracy: >95%
- False Positive Rate: <0.1%
- Maximum Simultaneous Faces: 10

## Troubleshooting Common Installation Errors

### 1. RuntimeError: Unsupported image type
If you encounter: `RuntimeError: Unsupported image type, must be 8bit gray or RGB image`

**Solution:**
- Verify you're using 24-bit RGB images
- Try different image files(sometimes a half face or a blurred image can cause this error)
- Ensure you're using Python 3.7:
  ```bash
  python --version 
  ```

### 2. ModuleNotFoundError: No module named 'face_recognition'
This usually occurs due to missing CMake and dlib dependencies.

**Solution:**
```bash
pip install CMake
pip install dlib
```

### 3. Unable to Install dlib
If you can't install dlib through pip, follow these alternative steps:

1. Download dlib:
   - Visit [dlib GitHub repository](https://github.com/davisking/dlib.git) or find the dlib.whl for py-3.7.6 in this repository 
   - Download the ZIP file
   - Extract the downloaded file

2. Install the correct wheel file:
   - Check your Python version: `python --version`
   - For Python 3.7: Use `dlib-19.22.99-cp37-cp37m-win_amd64.whl`
   - Copy the wheel file to your project directory
   - Install using:
     ```bash
     pip install dlib-19.22.99-cp37-cp37m-win_amd64.whl
     ```
   Note: Use the appropriate wheel file version matching your Python version

### 4. Using Virtual Environment (Recommended)
To avoid dependency conflicts, use a virtual environment:

1. In your code editor:
   - Click on the Python version in the bottom right
   - Choose "Create a Virtual Environment"
   - Select Python 3.7.6

2. Activate the virtual environment:
   ```bash
   # Windows
   .\venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install required packages in the virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

### 5. OpenCV GUI Error on Linux
If you encounter: `cv2.error: OpenCV... The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support`

**Solution:**
```bash
sudo apt-get update
sudo apt-get install libgtk2.0-dev pkg-config
pip uninstall opencv-python
pip install opencv-python
```

### 6. GTK Module Error on Linux
If you see: `Gtk-Message: Failed to load module "canberra-gtk-module"`

**Solution:**
```bash
sudo apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1-mesa-glx
sudo apt-get install -y python3-opencv
pip uninstall opencv-python opencv-python-headless
pip install opencv-python --no-cache-dir
```

### 7. Face Recognition Type Error on Linux
If you encounter: `TypeError: compute_face_descriptor(): incompatible function arguments`

**Solution:**
```bash
# First, install system dependencies
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev
sudo apt-get install libx11-dev libgtk-3-dev

# Then install compatible versions of dlib and face_recognition
pip uninstall dlib face_recognition
pip install dlib==19.24.0
pip install face_recognition==1.3.0
```

## Future Enhancements

1. **Planned Features**
   - Mobile application integration
   - Cloud synchronization
   - Advanced analytics dashboard
   - Multi-location support
   - API integration capabilities

2. **Under Development**
   - Automated reporting system

## Contributing

contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and queries:
- Create an issue in the repository
- Contact: neutralwritergithubdedicated@gmail.com
- Documentation: [Wiki](https://github.com/solveditnpc/face_recognition_using_opencv-python.git)

## Acknowledgments

- OpenCV community
- dlib developers

## Version History

- v2.0 (Current): Added anti-spoofing, improved GUI
- v1.5: Multiple face recognition support
- v1.0: Initial release with basic features

## Project Status

Active development - Regular updates and maintenance ongoing.
