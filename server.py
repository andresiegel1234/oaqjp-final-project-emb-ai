from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    text = request.args.get('text', 'I think I am having fun')
    
    # Beispielhafte Emotionserkennung (statische Werte)
    emotions = {
        'anger': 0.01,
        'disgust': 0.005,
        'fear': 0.02,
        'joy': 0.95,
        'sadness': 0.015
    }
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    response = {
        'text': text,
        'emotions': emotions,
        'dominant_emotion': dominant_emotion
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)