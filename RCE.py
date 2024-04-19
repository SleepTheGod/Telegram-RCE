import cv2
import os
# Get the file ID from the Telegram message
file_id = message.document.file_id
# Download the file from Telegramfile_path = os.path.join(os.getcwd(), 'downloaded_video.mp4')
downloaded_file = bot.get_file(file_id)downloaded_file.download(file_path)
# Create a VideoCapture object
cap = cv2.VideoCapture(file_path)
# Check if camera opened successfullyif not cap.isOpened():
    print("Error opening video stream")
# Create a VideoWriter object to save the videowriter = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15, (640,480))
# Read until video is completed
while cap.isOpened():    # Capture frame-by-frame
    ret, frame = cap.read()
    # Check if frame was successfully captured    if not ret:
        break
    # Display the resulting frame    cv2.imshow('frame', frame)
    # Write the frame to the video file
    writer.write(frame)
    # Wait for a key press, and if 'q' is pressed, break the loop    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the capture and destroy all windows
cap.release()
writer.release()cv2.destroyAllWindows()
# Delete the downloaded video file to save space
os.remove(file_path)
