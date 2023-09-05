import numpy as np
import cv2

def fill_frame(frame):
    h, w = frame.shape[0], frame.shape[1]
    if h > w:
        _pad = np.zeros([h, int((h - w) / 2), 3])
        frame = np.concatenate([_pad, frame, _pad], axis=1)
    elif h < w:
        _pad = np.zeros([int((w - h) / 2), w, 3])
        frame = np.concatenate([_pad, frame, _pad], axis=0)
        frame = np.transpose(frame, [1, 0, 2])
    frame = cv2.resize(frame, (1024, 1024))
    return frame