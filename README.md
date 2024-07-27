
# Face Recognition

This project helps compare faces from live camera feed to your existing database, The associated names with the identified faces are then added with the identification time and date to an excel sheet for easy access


## Deployment

To deploy this project 

```bash
  open cmd in your project folder 
  python -m venv nameofyourvenv    
  nameofyourvenv/Scripts/activate
  pip install opencv
  pip install face_recognition
  run attendance_opencv.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your venv 

`face_recognition-1.3.0`

`python 3.7.6`

`CMake-3.29.6`

`dlib-19.22.99`

`numpy-1.21.6`



## Installation Error

You may encounter the following errors 

```bash
  1) RuntimeError: Unsupported image type, must be 8bit gray or RGB image.
  solution- check if you are importing a 24bit rgb image and try a few different images 
            python --version 
            it must be set to 3.7 
  2) ModuleNotFoundError: No module named 'face_recognition'
  solution- you are missing CMake and dlib which in turn prompted this error
            pip install CMake
            pip install dlib
            if you are still unable to install dlib then move to third solution
  3) alternative to dlib error 
  solution- open https://github.com/davisking/dlib.git in your browser and download zip file 
            extract the file from downloads 
            go to your project directory
            check py version (python --version)
            since we are running python 3.7.6 
            we will need dlib-19.22.99-cp37-cp37m-win_amd64.whl
            copy dlib-19.22.99-cp37-cp37m-win_amd64.whl to your project directory from extracted files 
            now open cmd in project directory and run pip install dlib-19.22.99-cp37-cp37m-win_amd64.whl
            you need to install the correct version of dlib as per your python version
  4) you can also create a virtual environment by following these steps 
            open your code editor 
            click on python version written on bottom right 
            choose "create a virtual environment"
            now choose python 3.7.6
            open cmd and install your modules as listed in Environment Variables

```
    
