import json
import unittest
from app.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def helper_check_emotion(self, text, expected_emotion):
        """Hilfsmethode, um doppelten Code zu vermeiden."""
        result_json = emotion_detector(text)
        try:
            result = json.loads(result_json)
            dominant_emotion = (
                result.get("document_tone", {})
                .get("tones", [{}])[0]
                .get("tone_id", "")
            )
        except Exception as e:
            self.fail(f"Failed to parse JSON response: {e}")

        self.assertEqual(
            dominant_emotion,
            expected_emotion,
            f"Text: '{text}' - Expected: '{expected_emotion}', Got: '{dominant_emotion}'",
        )

    # Ab hier wird jede Emotion als einzelner Test definiert:
    def test_joy(self):
        self.helper_check_emotion("I am glad this happened", "joy")

    def test_anger(self):
        self.helper_check_emotion("I am really mad about this", "anger")

    def test_disgust(self):
        self.helper_check_emotion(
            "I feel disgusted just hearing about this", "disgust"
        )

    def test_sadness(self):
        self.helper_check_emotion("I am so sad about this", "sadness")

    def test_fear(self):
        self.helper_check_emotion(
            "I am really afraid that this will happen", "fear"
        )


if __name__ == "__main__":
    unittest.main()