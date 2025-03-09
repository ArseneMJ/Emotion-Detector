import requests
import asyncio
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
async def detect_emotion() :
    try:
        text_to_analyze = request.args.get('textToAnalyze')
        if(text_to_analyze ==''):
            return ' Invalid text! Please try again!',40
        emotion_data = await emotion_detector(text_to_analyze)
        respond = f"For the given statement, the system response is 'anger': {emotion_data['anger']}, 'disgust': {emotion_data['disgust']}, 'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']}, 'sadness': {emotion_data['sadness']}. The dominant emotion is {emotion_data['dominant_emotion']}."
        return respond,200
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}",500



if __name__ == '__main__':
    app.run( port=5000,debug=True)
