Steps that I followed to finish the given assignment
1) Virtual Environment Setup
	Created a folder named Internship
		Inside that create another folder Assignment_1
  Now opened this folder 'Assignment_1' in VS Code.
  Opened the terminal and typed
  python -m venv /path/to/new/virtual/environment

2) To enable the Activate.ps1 setting the execution policy for the user.
	C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3) Then activating the virtual environment
	PS D:\Internship\Assignment_1> . .\venv\Scripts\Activate.ps1

4) Installing ultralytics
	(venv) PS D:\IIITH_internship\Assignment_1> pip install ultralytics; 

5) Save the given image in the Assignment_1 folder as  'bus.jpg'
6) Run the Script
	from ultralytics import YOLO

	from ultralytics import YOLO

	# Load the YOLOv8n model	
	model = YOLO("yolov8n.pt")

	# Predict on your local image
	results = model("D:\\Internship\\Assignment_1\\bus.jpg")

	# Show results
	results[0].show()       # Optional: Display window with results
	results[0].save()       

6) Output image is displayed. You can also check the output in the Assignments_1 folder. A file named 'result_bus.png' is the desired output image.

NOTE:
Instead of step 6 if you directly type 
	yolo task=detect mode=predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
in the yolo terminal 
Then the output image is stored in runs\detect\predict
