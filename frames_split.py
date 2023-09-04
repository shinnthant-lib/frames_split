import cv2 
import os

video_path=os.joint("video","name.mp4")
frames_dir="frames"


vidcap = cv2.VideoCapture(video_path)
frame_len=int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
nof=150


frame_c = 1
capframe=frame_len//nof
countdown=1

success,image = vidcap.read()
while success:
    if countdown==capframe:
        frame_path=os.joint(frames_dir,f"{str(frame_c).zfill(0)}.jpg")
        cv2.imwrite(frame_path,image)
        frame_c += 1
        countdown=0
    else:
        countdown+=1
    success,image = vidcap.read()