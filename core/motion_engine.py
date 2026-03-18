import cv2
import mediapipe as mp
# استدعاء مباشر للمكونات لضمان عدم حدوث AttributeError
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_draw

class FlashDealMotionEngine:
    def __init__(self):
        # إعداد حلول تتبع اليد
        self.mp_hands = mp_hands
        self.mp_draw = mp_draw
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )

    def verify_motion(self, frame):
        """
        معالجة الصورة لرصد بصمة الحركة (نقاط اليد)
        """
        if frame is None:
            return False, None

        # تحويل الصورة إلى RGB لأن MediaPipe يتعامل مع هذا النظام
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        motion_detected = False
        
        if results.multi_hand_landmarks:
            motion_detected = True
            # رسم الهيكل العظمي للبصمة الحركية على الصورة
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    self.mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2)
                )
        
        return motion_detected, frame
