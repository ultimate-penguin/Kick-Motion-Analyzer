## 🥋 Kick Motion Analyzer

A Streamlit-based computer vision application that analyzes martial arts kicking techniques from uploaded videos. The app estimates knee joint angles throughout the kick, calculates angular velocity, visualizes movement over time, and provides summary statistics to help evaluate kicking performance.Additionally, a plot of left and right hip's vertical positions over time is included to visualize spinning kicks.

This project demonstrates the application of pose estimation, biomechanics, and interactive data visualization for sports performance analysis.

## Features
 ```
📹 Upload a martial arts kick video
🦵 Automatically detect left and right knee joint positions using pose estimation
📈 Plot knee joint angles over time (degrees)
⚡ Compute and visualize angular velocity (degrees/second)
📊 Display descriptive statistics including:
    -Peak knee angle
	  -Peak angular velocity
	  -Range of motion (ROM)
	  -Mean joint angle
📈 Plot hip's vertical positions over time
📥 Download the raw data as a CSV file
🌐 Interactive web interface built with Streamlit
 ```
## Workflow
	  -Upload a kick video.
	  -The application performs pose estimation on each video frame.
	  -Knee joint angles are calculated throughout the movement.
	  -Angular velocity is derived from the angle time series.
	  -Interactive plots display:
		    -Left knee angle vs time
		    -Right knee angle vs time
		    -Left knee angular velocity vs time
		    -Right knee angular velocity vs time
		    -Hip's vertical positions vs time
		    -Summary statistics are generated.
		    -Export raw data as a CSV file.


For both the left and right knees, the application computes:
 ```
  -Maximum (Peak) Joint Angle\
  -Maximum Angular Velocity\
  -Mean Joint Angle\
  -Range of Motion (ROM)\
 ```
The knee joints' angular velocities are approximated by the formulas:
      
	ω ≈ (θᵢ-θᵢ₋₁)*fps


## Technologies Used
	-Python
	-Streamlit
	-OpenCV
	-yolov8n-pose 
	-NumPy
	-Pandas
	-Plotly

## Project Structure
 ```
Kick_analytics/  

├── kick_analytic_app.py  

├── analysis_script.py  

├── requirements.txt  

└── README.md  

|__LICENSE
 ```
## Installation
 ```
Clone the repository:

git clone https://github.com/ultimate-penguin/Kick-Motion-Analyzer.git

cd Kick-Motion-Analyzer


Install the required packages:

pip install -r requirements.txt


Run the application:

streamlit run kick_analytic_app.py
 ```
**Output**



The application generates:

	-Knee angle plots over time
	-Angular velocity plots
	-Hip vertical position plots
	-Summary statistics 
	-Downloadable CSV containing frame-by-frame measurements

Example Output:\
<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/57540ab6-5e36-498a-9869-aab1facc0e96" />
<img width="250" height="250" alt="kick3" src="https://github.com/user-attachments/assets/829d0593-17c1-4c28-bc92-9890a67464f9" />
<img width="250" height="250" alt="kick5" src="https://github.com/user-attachments/assets/e3748bac-4a34-4fc0-8e16-11e9d21d619f" />

## Applications

This project can be used for:

	-Martial arts technique analysis

	-Athlete performance monitoring

	-Movement quality assessment

**Limitations**

	-The script was written to detect and calculate motions of only one person. It might fail if there are multiple people in the video.
	-The model sometimes fails to output accurate keypoints during the kick motion resulting in incorrect movement data.

**Future Improvements**

	-Improve model to output more accurate keypoints
	-Improve the script to handle multiple people detections and motion analysis
	-Detect different kick types automatically
	-Identify key events (chamber, impact, recovery)
	-Support real-time webcam analysis

## Author

**Ultimate Penguin**

GitHub: https://github.com/ultimate-penguin


