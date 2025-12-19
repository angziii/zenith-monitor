import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import threading
import time
import os

class VisionEngine:
    def __init__(self, camera_index=None):
        if camera_index is None:
            camera_index = int(os.environ.get("CAMERA_INDEX", 0))
            
        base_options = python.BaseOptions(model_asset_path='face_landmarker.task')
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            running_mode=vision.RunningMode.IMAGE,
            num_faces=1
        )
        self.detector = vision.FaceLandmarker.create_from_options(options)
        self.cap = cv2.VideoCapture(camera_index)
        self.focus_score = 100.0
        self.face_detected = False
        self.is_running = False
        self._thread = None
        
        # New: Temporal smoothing
        self.score_history = [] 
        self.max_history = 10

    def start(self):
        self.is_running = True
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self.is_running = False
        if self._thread:
            self._thread.join()
        if self.cap.isOpened():
            self.cap.release()

    def _run(self):
        while self.is_running:
            success, frame = self.cap.read()
            if not success:
                time.sleep(0.1)
                continue

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            detection_result = self.detector.detect(mp_image)

            raw_score = 0.0
            if detection_result.face_landmarks:
                self.face_detected = True
                
                # 1. Base Score from Head Pose
                pose_score = 100.0
                if detection_result.facial_transformation_matrixes:
                    matrix = detection_result.facial_transformation_matrixes[0]
                    yaw = np.arctan2(matrix[0, 2], matrix[2, 2]) * 180 / np.pi
                    pitch = np.arcsin(-matrix[1, 2]) * 180 / np.pi
                    
                    # More granular penalty: starts dropping after 10 degrees, steeper after 25
                    total_dev = np.sqrt(yaw**2 + pitch**2)
                    if total_dev > 10:
                        pose_score -= (total_dev - 10) * 2.5
                
                # 2. Eye Tracking Blendshapes
                eye_penalty = 0.0
                if detection_result.face_blendshapes:
                    # MediaPipe Blendshapes (0-1 range): 
                    # 9: eyeLookDownLeft, 10: eyeLookDownRight, 13: eyeLookOutLeft, etc.
                    blendshapes = {b.category_name: b.score for b in detection_result.face_blendshapes[0]}
                    
                    # Detect looking down (typical phone use) or side-eyeing
                    look_down = (blendshapes.get('eyeLookDownLeft', 0) + blendshapes.get('eyeLookDownRight', 0)) / 2
                    look_side = (blendshapes.get('eyeLookOutLeft', 0) + blendshapes.get('eyeLookInRight', 0)) / 2
                    
                    if look_down > 0.4:
                        eye_penalty += (look_down - 0.4) * 50
                    if look_side > 0.5:
                        eye_penalty += (look_side - 0.5) * 40
                
                raw_score = max(0, pose_score - eye_penalty)
            else:
                self.face_detected = False
                raw_score = 0.0

            # 3. Smoothing (Moving Average)
            self.score_history.append(raw_score)
            if len(self.score_history) > self.max_history:
                self.score_history.pop(0)
            
            self.focus_score = sum(self.score_history) / len(self.score_history)
            
            time.sleep(0.05)

    def get_status(self):
        return {
            "focus_score": round(self.focus_score, 2),
            "face_detected": self.face_detected
        }

if __name__ == "__main__":
    vision_engine = VisionEngine()
    vision_engine.start()
    try:
        while True:
            print(vision_engine.get_status())
            time.sleep(1)
    except KeyboardInterrupt:
        vision_engine.stop()
