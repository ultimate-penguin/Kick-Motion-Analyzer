from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from pathlib import Path
import imageio.v3 as iio
def compute_angle(start,middle,end):
  vector1 = middle-start
  vector2=end-middle
  dot_product = np.dot(vector1,vector2)
  mag_v1 = np.linalg.norm(vector1)
  mag_v2 = np.linalg.norm(vector2)
  cos_angle = dot_product/(mag_v1*mag_v2)
  angle_rad=np.arccos(np.clip(cos_angle,-1,1))
  angle_deg = np.degrees(angle_rad)
  return angle_deg



def analyze_video(path):
    PROJECT_ROOT = Path(__file__).parent
    model =YOLO('yolov8n-pose.pt')
    cap = cv2.VideoCapture(path)
    frames=[]
    # Get frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps=cap.get(cv2.CAP_PROP_FPS)
 

    frame_count=0
    angleL=0
    anglesL=[]
    anglesR=[]
    time=[]
    omegasL=[]
    omegasR=[]
    LH=[]
    RH=[]
    
    while cap.isOpened():
        ret,frame= cap.read()
        if not ret:
            break
        frame_count+=1
    
        results = model(frame,conf=0.85)
        keypoints =results[0].keypoints.xy.cpu().numpy()

    
        annotated_image = results[0].plot()
        
        if len(keypoints)==0:
          continue
        angleL=compute_angle(keypoints[0][11],keypoints[0][13],keypoints[0][15])
        angleR=compute_angle(keypoints[0][12],keypoints[0][14],keypoints[0][16])
        left_hip = keypoints[0][11][1]
        right_hip = keypoints[0][12][1]
        h, w, _ = annotated_image.shape
        text_x = int(w * 0.05) # 5% from left
        text_y = int(h * 0.05) + 50 # 5% from top, plus some offset for font size

        anglesL.append(angleL)
        anglesR.append(angleR)
        LH.append(left_hip)
        RH.append(right_hip)
        time.append(frame_count/fps)
        if len(anglesL)<2:
            omegaL=0
            omegaR=0
            omegasL.append(0)
            omegasR.append(0)
        else:
            omegaL= fps*(angleL-anglesL[-2])
            omegasL.append(omegaL)
            omegaR= fps*(angleR-anglesR[-2])
            omegasR.append(omegaR)
        
        cv2.putText(annotated_image,f'left knee:{round(angleL)}',(text_x-25, text_y-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),3,cv2.LINE_AA) 
        cv2.putText(annotated_image,f'right knee:{round(angleR)}',(text_x+100, text_y-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),3,cv2.LINE_AA)
        cv2.putText(annotated_image,f'left speed:{round(omegaL)}',(text_x-25, text_y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),3,cv2.LINE_AA)
        cv2.putText(annotated_image,f'right speed:{round(omegaR)}',(text_x+100, text_y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),3,cv2.LINE_AA)
        rgb_frame = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        frames.append(rgb_frame)
        
    cap.release()
    
    output_path = "output.mp4"
    iio.imwrite(output_path, frames, fps=fps, codec="libx264", pixelformat="yuv420p")

    d = {'annot_video':output_path,'right leg angle': anglesR,'left leg angle':anglesL,'right leg speed':omegasR,'left leg speed':omegasL,'left hip pos':LH,'right hip pos':RH,'time':time}
    return d
