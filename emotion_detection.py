import requests


def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Constructing the request payload
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Custom header specifying the model ID
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        # Sending a POST request to the emotion detection API
        response = requests.post(url, json=myobj, headers=header)

        # Checking if the request was successful
        response.raise_for_status()

        # EXPECTATION MET: Returning the exact text attribute of the response object
        return response.text

    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"


# --- Example Execution ---
if __name__ == "__main__":
    text_to_analyze = "I love this new technology."
    raw_response_text = emotion_detector(text_to_analyze)

    print("Returned Value (Type:", type(raw_response_text), "):")
    print(raw_response_text)