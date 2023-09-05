import cv2 
import os
import numpy as np




video_path=os.path.join("video","vic.mp4")
frames_dir="frames"


vidcap = cv2.VideoCapture(video_path)
frame_len=int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
nof=150


if not os.path.exists(frames_dir): 
    os.mkdir(frames_dir)

frame_c = 1
capframe=frame_len//nof
countdown=1

success,frame = vidcap.read()
while success:
    if countdown==capframe:
        h, w = frame.shape[0], frame.shape[1]
        if h > w:
            _pad = np.zeros([h, int((h - w) / 2), 3])
            frame = np.concatenate([_pad, frame, _pad], axis=1)
        elif h < w:
            _pad = np.zeros([int((w - h) / 2), w, 3])
            frame = np.concatenate([_pad, frame, _pad], axis=0)
            frame = np.transpose(frame, [1, 0, 2])
        frame = cv2.resize(frame, (1024, 1024))
        
        frame_path=os.path.join(frames_dir,f"{str(frame_c).zfill(0)}.jpg")
        cv2.imwrite(frame_path,frame)
        frame_c += 1
        countdown=0
    else:
        countdown+=1
    success,frame = vidcap.read()

