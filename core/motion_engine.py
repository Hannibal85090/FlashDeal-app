import cv2
import numpy as np
import mediapipe as mp

class FlashDealMotionEngine:
    def __init__(self):
        """إعداد محرك رصد بصمة الحركة - FlashDeal Star"""
        # الوصول المباشر للحلول لضمان التوافق مع Streamlit Cloud
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )

    def verify_motion(self, frame):
        """التحقق من بصمة الحركة ورسم نقاط الاتصال"""
        if frame is None:
            return False, None

        # تحويل الصورة إلى RGB للمعالجة
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        motion_detected = False
        if results.multi_hand_landmarks:
            motion_detected = True
            for hand_landmarks in results.multi_hand_landmarks:
                # رسم الهيكل العظمي لليد كبصمة أمان حركية
                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    self.mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2)
                )
        
        return motion_detected, frame
