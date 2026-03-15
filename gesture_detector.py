import cv2
import mediapipe as mp
import math

class GestureDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hands.process(rgb)

        hands_data = []

        if not result.multi_hand_landmarks:
            return hands_data

        for hand in result.multi_hand_landmarks:

            fingers = self.count_fingers(hand)
            pinch = self.detect_pinch(hand)
            x = hand.landmark[0].x

            hands_data.append({
                "fingers": fingers,
                "pinch": pinch,
                "x": x
            })

        return hands_data


    def count_fingers(self, hand):

        tips = [8,12,16,20]

        count = 0

        for tip in tips:

            if hand.landmark[tip].y < hand.landmark[tip-2].y:
                count += 1

        return count


    def detect_pinch(self, hand):

        thumb = hand.landmark[4]
        index = hand.landmark[8]

        distance = math.sqrt(
            (thumb.x-index.x)**2 +
            (thumb.y-index.y)**2
        )

        return distance < 0.07