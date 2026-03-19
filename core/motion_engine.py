import cv2
import mediapipe as mp

class MotionEngine:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5
        )

    def process_frame(self, frame):
        # تحويل الألوان لمعالجة mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        return results

# نسخة جاهزة للاستخدام
engine = MotionEngine()
