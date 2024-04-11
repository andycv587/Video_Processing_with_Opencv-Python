# OpenCV Installation and Usage Guide<br>

This guide provides instructions for installing OpenCV on Windows, macOS, and Linux, and demonstrates basic usage scenarios such as reading an image, reading a video, and extracting and saving frames from a video.<br><br>

## Installation<br>

### Windows<br>

1. Open a command prompt and ensure that Python and pip are installed:<br>

```console
python --version
pip --version
```

If Python is not installed, download and install it from the [official website](https://www.python.org/downloads/windows/).<br>

2. Install OpenCV using pip:<br>

```console
pip install opencv-python
pip install opencv-contrib-python
```

### macOS<br>

1. Open a terminal window and ensure that Python and pip are installed:<br>

```console
python3 --version
pip3 --version
```

If Python is not installed, install it using [Homebrew](https://brew.sh/):<br>

```console
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

2. Install OpenCV using pip:<br>

```console
pip3 install opencv-python
```

### Linux<br>

1. Open a terminal window and ensure that Python and pip are installed:<br>

```console
python3 --version
pip3 --version
```

If Python is not installed, install it using your distribution's package manager (e.g., apt for Ubuntu, dnf for Fedora).<br>

2. Install OpenCV using pip:<br>

```console
pip3 install opencv-python
```

## Usage<br>

### Reading an Image<br>

To read an image and display it:<br>

```python
import cv2

# Load an image
image = cv2.imread('path_to_your_image.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```


Replace 'path_to_your_image.jpg' with the path to your image.<br>

### Reading a Video<br>
To read a video and play it:<br>

```python

import cv2

# Open the video
cap = cv2.VideoCapture('path_to_your_video.mp4')

# Read and display each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()

```

Replace 'path_to_your_video.mp4' with the path to your video.<br>

### Saving Video Frames<br>
To extract and save frames from a video:<br>

```python

import cv2
import os

def save_video_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(output_folder, f"frame_{frame_count:04d}.jpg"), frame)
        frame_count += 1
    cap.release()
    print(f"Extracted {frame_count} frames.")

```

# Example usage
```python
save_video_frames('path_to_your_video.mp4', 'frames_output')
```

Replace 'path_to_your_video.mp4' with the path to your video, and 'frames_output' with your desired output directory.<br>

Conclusion<br>
This guide has introduced how to install OpenCV and use it for basic image and video processing tasks. For more advanced features and usage, refer to the OpenCV documentation.<br>




