import requests,asyncio
async def emotion_detector(text_to_analyze):
        url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        inputJson={ "raw_document": { "text": text_to_analyze }}
        try:
            response = requests.post(url, headers=headers, json=inputJson)
            if response.status_code == 400:
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }

            response_data = response.json()
            emotions = response_data['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            emotions['dominant_emotion'] = dominant_emotion 

            return emotions

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None