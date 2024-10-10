import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detection(self):
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }

        for statement, expected_dominant_emotion in test_cases.items():
            with self.subTest(statement=statement):
                response = emotion_detector(statement)
                dominant_emotion = response['dominant_emotion']
                self.assertEqual(dominant_emotion, expected_dominant_emotion, 
                                 f"Expected dominant emotion for '{statement}' to be '{expected_dominant_emotion}', but got '{dominant_emotion}'.")

if __name__ == '__main__':
    unittest.main()
