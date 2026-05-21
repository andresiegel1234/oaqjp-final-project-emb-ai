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

        # Convert response text into a dictionary
        response_dict = json.loads(response.text)

        # Drill down to the inner emotion scores
        emotions = response_dict["emotionPredictions"][0]["emotion"]

        # Extract individual scores
        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Determine the dominant emotion (the key with the maximum value)
        dominant_emotion = max(emotions, key=emotions.get)

        # Construct and return the exact requested dictionary format
        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion,
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}
    except (KeyError, IndexError):
        return {"error": "Unexpected API response format."}


# --- Example Execution ---
if __name__ == "__main__":
    text = "I'm so happy I am doing this"
    output = emotion_detector(text)

    print(json.dumps(output, indent=4))


