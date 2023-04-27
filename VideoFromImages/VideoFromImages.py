
import cv2
import os

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'H264')  # You can choose any codec here
fps = 30.0  # Define the frame rate of the output video
out = cv2.VideoWriter('output.mp4', fourcc, fps, (640, 480))  # Set the video output file name, codec, frame rate and video size here

# Path of the folder containing images
path = 'images'

# Loop through all the files in the folder
for filename in os.listdir(path):
    if filename.endswith('.jpg'):  # You can choose any image format here
        # Read the image file
        img = cv2.imread(os.path.join(path, filename))
        # Write the image to the video file
        out.write(img)

# Release the VideoWriter object and close the output file
out.release()
