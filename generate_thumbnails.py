import cv2
import os

def generate_thumbnail(video_path):
    # Capture the video
    cap = cv2.VideoCapture(video_path)
    success, image = cap.read()

    if success:
        # Create a thumbnail filename by removing the video extension
        thumbnail_filename = os.path.splitext(video_path)[0] + ".png"
        cv2.imwrite(thumbnail_filename, image)

    cap.release()

def main():
    folder_path = './features'  # Relative path to the 'features' folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mov')):  # Add other video formats if needed
            video_path = os.path.join(folder_path, filename)
            generate_thumbnail(video_path)

if __name__ == "__main__":
    main()
