import cv2
import os

# Set the FFmpeg options for handling RTSP streams
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# Your camera's RTSP URL
rtsp_url = "rtsp://admin:Aa12345678@192.168.1.22/onvif1"

# Create a VideoCapture object with the FFMPEG backend
vcap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

if not vcap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Video stream opened successfully.")

while vcap.isOpened():
    # Read a frame from the video stream
    ret, frame = vcap.read()

    # Check if the frame was retrieved successfully
    if not ret:
        print("Error: Can't receive frame (stream may have ended). Exiting ...")
        break

    # Display the frame in a window
    cv2.imshow('RTSP Stream', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
vcap.release()
cv2.destroyAllWindows()
