
from moviepy.editor import ImageSequenceClip
import os


# Path of the folder containing images
path = 'videoplayback'

# Load all the images as a list
image_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

print(len(image_files))
# Create a clip from the images
clip = ImageSequenceClip(image_files, fps=30)

# Write the clip to a video file
clip.write_videofile('output1.mp4')
