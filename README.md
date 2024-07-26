# Intrusion Detection System with OpenCV

## Overview

This project implements an Intrusion Detection System (IDS) using OpenCV and the Pose Detection module from `cvzone`. It captures video from a webcam, detects human presence using pose detection, and sends an alert with an image when suspicious activity is detected.

## Features

- Real-time human pose detection using OpenCV and `cvzone`.
- Alerts sent via SMS using Twilio, including an image of the detected intrusion.
- Dynamic image upload to cloud storage for accessing the image URL.

## Requirements

- Python 3.x
- OpenCV
- `cvzone`
- `mediapipe`
- `twilio`
- Cloud storage service (e.g., AWS S3) for image hosting

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kamlesh616/intrusion-detection-system.git
   cd intrusion-detection-system
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment:**

   - Obtain your Twilio account SID and Auth Token from the Twilio Console.
   - Configure your cloud storage service and get credentials.

## Configuration

1. **Twilio Setup:**
   - Update `send.py` with your Twilio account SID, Auth Token, and phone numbers.

   ```python
   account_sid = 'your_actual_account_sid'
   auth_token = 'your_actual_auth_token'
   ```

2. **Cloud Storage:**
   - Modify `main.py` to use your cloud storage service for uploading images. Ensure the image URL is publicly accessible.

## Usage

1. **Run the IDS:**

   ```bash
   python main.py
   ```

2. **The system will:**
   - Capture video from your webcam.
   - Detect human presence using pose detection.
   - Save images of detected intrusions.
   - Upload images to cloud storage.
   - Send an SMS with an image URL when intrusion is detected.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!
