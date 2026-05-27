import json
import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()

        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Die dominante Emotion ermitteln (z.B. 'joy')
        dominant_emotion = max(emotions, key=emotions.get)

        # JSON so wie es 'test_emotion_detection.py' verlangt!
        result = {
            "document_tone": {
                "tones": [
                    {
                        "tone_id": dominant_emotion,
                        "score": emotions[dominant_emotion],
                    }
                ]
            }
        }

        # Als JSON-String zurückgeben
        return json.dumps(result)

    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"