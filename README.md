**Project Overview**
This project is an Object Finder designed to help users quickly locate commonly misplaced items such as keys, remotes, and wallets.
It is also specialized for deaf and hard‑of‑hearing users, because the system speaks the name of the detected object aloud using text‑to‑speech.
The model is trained using a Roboflow Universe dataset dataset and runs in real time through a webcam.

**Files Included in This Repository**

1. `detect.py`
This is the main Python script that runs the object detection system.  
It loads the trained YOLO model, opens the webcam, detects objects frame‑by‑frame, draws bounding boxes, and speaks the detected object name aloud.

2. `best.pt`
This is the **trained YOLO model** produced after training the dataset in Google Colab.  
It contains the learned weights for detecting keys, remotes, and wallets.

3. `SDET102_final_project.ipynb`
This is the **Google Colab notebook** used to train the model.  
It includes dataset download, YOLO training code, and training configuration.

4. `multiobject.v2-my-finder.yolo26.zip`
This ZIP file contains the **Roboflow dataset** used for training.  
It includes images, labels, and the `data.yaml` file required for YOLO training.

**How to Run the Code**

1. Install required libraries
   Run the following in your terminal:

   ```
   pip install ultralytics opencv-python pyttsx3
   ```

2. Place the model file
   Ensure `best.pt` is in the same folder as `detect.py`.

3. Run the detection script
   In Visual Studio Code or any terminal:

   ```
   python detect.py
   ```

4. Use the system
   - The webcam will open  
   - When an object is detected, a bounding box appears  
   - The system speaks the object name aloud
   - Press Q to quit

**Required Libraries**
The project uses the following Python libraries:

ultralytics           – for YOLO model loading and inference  
opencv-python (cv2)   – for webcam access and drawing bounding boxes  
pyttsx3               – for text‑to‑speech output  
time                  – for timing control in speech output  

All libraries can be installed using pip.

**Input Data Source**
The dataset was created and labeled using Roboflow.  
It includes images of:

- Keys  
- Remotes  
- Wallets  

The dataset was exported in YOLO26 format and downloaded directly in the Colab notebook using the Roboflow API.

**How the Model Was Trained**

Training was performed in Google Colab using:

- YOLOv8n (nano model)  
- 30 epochs  
- Image size 640  
- Batch size 16  

The training notebook (`SDET102_final_project.ipynb`) contains:

- Dataset download  
- Model initialization  
- Training loop  
- Output metrics and saved weights  

The final trained model is saved as `best.pt`.

**Limitations / Special Notes**
- The model is trained on three specific objects only: keys, remote, wallet.  
- Detection accuracy depends on lighting and camera quality.  
- The system speaks only the highest‑confidence object per frame.  
- Background clutter or overlapping objects may reduce accuracy.  
- The webcam must be connected and accessible for the script to run.  
- The text‑to‑speech engine may behave differently on macOS vs Windows.
- The system detects objects in order, meaning it will not repeat the same object unless you show a different object first.
  
