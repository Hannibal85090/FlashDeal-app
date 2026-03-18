import cv2
import numpy as np
import mediapipe as mp

class FlashDealMotionEngine:
    def __init__(self):
        # استخدام الاستدعاء المباشر من mp.solutions لتجنب AttributeError
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )

    def verify_motion(self, frame):
        if frame is None:
            return False, None

        # تحويل الصورة إلى RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        motion_detected = False
        if results.multi_hand_landmarks:
            motion_detected = True
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS
                )
        
        return motion_detected, frame
