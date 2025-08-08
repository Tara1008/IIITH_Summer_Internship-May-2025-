import cv2
import os

image_folder = "D:\IIITH_internship\Assignment_2\processed"
video_name = "D:\IIITH_internship\Assignment_2\output_video.mp4"
fps = 15  # Set to match original video's FPS

# Get sorted list of images
images = sorted([img for img in os.listdir(image_folder) if img.endswith((".jpg", ".png"))])
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = frame.shape

# Define video writer
out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

for image in images:
    frame = cv2.imread(os.path.join(image_folder, image))
    out.write(frame)

out.release()
print(f"✅ Final video saved as {video_name}")
