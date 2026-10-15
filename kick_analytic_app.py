import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from analysis_script import *
st.title('Martial Art Kick Analyzer')


uploaded_file = st.file_uploader(
    "Upload a kick video",
    type=["mp4", "mov", "avi"]
)

if uploaded_file is not None:

    with open("temp.mp4", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Analyzing video..."):
        results = analyze_video("temp.mp4")

    st.subheader("Annotated Video")
    with open(results['annot_video'], "rb") as f:
        st.video(f.read())

   

    st.write(results["annot_video"])
    
    st.subheader("Statistics")

    left = results["left leg angle"]
    right = results["right leg angle"]

    left_speed = results["left leg speed"]
    right_speed = results["right leg speed"]

    c1, c2, c3= st.columns(3)

    with c1:
      st.metric(
                "Left Max Angle",
                 f"{max(left):.1f}°"
                )

      st.metric(
                  "Left Peak Speed",
                  f"{max(left_speed):.1f}°/s"
                )
      st.metric(
                  "Left Mean Angle",
                  f"{sum(left)/len(left):.1f}°/s"
                )
      st.metric(
                  "Left Mean Speed",
                  f"{sum(left_speed)/len(left_speed):.1f}°/s"
                )

    with c2:

      st.metric(
                  "Right Max Angle",
                  f"{max(right):.1f}°"
                )

      st.metric(
                  "Right Peak Speed",
                  f"{max(right_speed):.1f}°/s"
                )
      st.metric(
                  "Right Mean Angle",
                  f"{sum(right)/len(right):.1f}°/s"
                )
      st.metric(
                  "Right Mean Speed",
                  f"{sum(right_speed)/len(right_speed):.1f}°/s"
                )


    with c3:

      st.metric(
                "Range of Motion Left",
                f"{max(left)-min(left):.1f}°"
                )

      st.metric(
                "Range of Motion Right",
                f"{max(right)-min(right):.1f}°"
                )
    st.subheader("Joint Angle")
    def plot_raw_data(key1,key2,name1,name2,title):
    
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=results['time'],y=results[key1],name=name1))
        fig.add_trace(go.Scatter(x=results['time'],y=results[key2],name=name2))
        fig.layout.update(title_text =title, xaxis_title="Time (Seconds)",xaxis_rangeslider_visible=True)
        
        

        st.plotly_chart(fig,use_container_width=True)

    plot_raw_data('left leg angle','right leg angle','Left Knee','Right Knee','knee angles(deg)')
    plot_raw_data('left leg speed','right leg speed','Left Knee','Right Knee','knee angular speed (deg/s)')
    plot_raw_data('left hip pos','right hip pos','Left Hip','Right Hip','Hip Position (y_position)')

    data = dict()
    
    for k,v in results.items():
        if k != 'annot_video':
            data[k] = v
    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
                        label="📥 Download Data as CSV",
                        data=csv_data,
                        file_name="kick_motions.csv",
                        mime="text/csv",
                       )
