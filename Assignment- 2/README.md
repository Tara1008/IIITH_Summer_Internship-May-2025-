# Video Frame Segmentation Task

This project takes a video input, extracts every 10th frame, performs segmentation (e.g., adding bounding boxes), and then reconstructs a new video from the processed frames.

---

## 📂 Folder Structure

```
project/
├── Shanghai.mp4             # Input video
├── frames/                  # Extracted frames will be saved here
│   ├── frame_0001.png
│   ├── frame_0002.png
│   └── ...
├── segmentation.py               # Script for image segmentation on frames
├── rebuilt.py               # Script to rebuild the video from processed frames
└── output/                  # Final output video saved here
```

---

## 🧰 Tools Used

- [FFmpeg](https://ffmpeg.org/) – for video-to-frames and frame-to-video conversion
- Python (with OpenCV, etc.) – for segmentation logic

---

## 🚀 Steps Followed

### 1. 📥 Download the Video
The input video `Shanghai.mp4` was downloaded and placed in the project directory.

---

### 2. 🎞 Extract Every 10th Frame Using FFmpeg

```bash
ffmpeg -i Shanghai.mp4 -vf "select=not(mod(n\,10))" -vsync vfr frames/frame_%04d.png
```

- This extracts every 10th frame and stores it in the `frames/` directory.
- Output files follow the format: `frame_0001.png`, `frame_0002.png`, ...

---

### 3. 🧠 Segment Each Extracted Frame

Run the segmentation script:

```bash
python segmentation.py
```

- This script processes the images in `frames/` and applies bounding box segmentation.
- It either overwrites or saves processed versions in a separate directory (as per your logic).

---

### 4. 🎬 Rebuild the Video from Processed Frames

Run the rebuild script:

```bash
python rebuilt.py
```

- This script collects all processed frames and compiles them back into a video.
- The final output video is saved in the `output/` directory.

---

## 🎯 Output

- ✅ Processed video with bounding boxes.
- 📁 Saved as a video file inside the `output/` directory.

---

## 📝 Notes

- Ensure FFmpeg is installed and available in your system’s PATH.
- Make sure required Python packages (e.g., `opencv-python`) are installed before running the scripts.

---

