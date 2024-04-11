# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:35:29 2024

@author: andyc
"""
import cv2
import os

def save_video_frames(video_path, output_folder):
    """
    Reads a video file and saves each frame as an image in the specified output folder.
    
    :param video_path: Path to the input video file.
    :param output_folder: Path to the folder where the frames will be saved.
    """
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
        if not ret:
            break
        
        # Save the frame to disk
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()
    print(f"Finished. Extracted {frame_count} frames.")

def process_frame(frame):
    """
    Process a single frame (for example, perform image segmentation).
    This method is currently empty but can be filled with processing logic.
    
    :param frame: The image frame to process.
    """
    # Example: Implement your image segmentation or processing logic here
    pass

# Example usage
if __name__ == "__main__":
    video_path = 'path_to_your_video.mp4'  # Update this to your video's path
    output_folder = 'frames_output'  # Update or keep this as your output directory
    save_video_frames(video_path, output_folder)
