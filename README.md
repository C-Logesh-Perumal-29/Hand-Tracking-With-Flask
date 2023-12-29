![HandTracking](https://github.com/C-Logesh-Perumal-29/Hand-Tracking-With-Flask/assets/125385633/61e0100b-5ce8-4738-931f-3bf234aa4670)

# Hand Tracking Webapp using Flask :

## Overview

This project implements a real-time hand tracking web application using Flask, Mediapipe, and OpenCV. The application captures video from the user's camera and utilizes the Mediapipe library to detect and track hand landmarks. The processed video stream is then displayed on a web page using Flask.

## Pre-requisites

**Ensure that you have the following libraries installed:**

  - Flask
  - OpenCV
  - MediaPipe

**You can install them using the following commands:**

  - `pip install Flask`
  - `pip install opencv-python`
  - `pip install mediapipe`

## Project Structure

  - **app.py:** The main Flask application file.
  - **templates/index.html:** HTML template for rendering the web page.

## Running the Application

  - Open a terminal and navigate to the project directory.
  - Run the following command to start the Flask application:

    `python app.py`

Open a web browser and go to http://localhost:5000 to access the application.

## Components

### 1. Flask Application (app.py)

**Routes:**

  - **/:** Renders the main web page.
  - **/video_feed:** Provides a video stream of hand tracking.
    
**Functions:**

  - **hand_tracking():** Implements the hand tracking functionality using MediaPipe and OpenCV.

### 2. HTML Template (templates/index.html)

  - Basic HTML structure for displaying the video stream.
    
### Hand Tracking Functionality

  - The hand_tracking function in app.py implements the hand tracking feature:

      - Initializes the MediaPipe Hands and OpenCV's VideoCapture.
    
      - Captures frames from the camera in a while loop.
    
      - Processes each frame using MediaPipe Hands to detect hand landmarks.
    
      - Draws hand landmarks and connections on the frame.
