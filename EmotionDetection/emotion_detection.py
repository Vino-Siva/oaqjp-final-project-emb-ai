import requests
import json

from typing import Dict, Optional

def emotion_detector(text_to_analyze: str) -> Optional[Dict[str, float]]:
    """
    Analyzes the given text to detect emotions and returns the intensity of 
    each emotion along with the dominant emotion.

    Parameters:
    text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
    dict: A dictionary containing the intensity of emotions ('anger', 
    'disgust', 'fear', 'joy', 'sadness') and the 'dominant_emotion'. 
    """
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = {"raw_document": {"text": text_to_analyze}}
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    if not text_to_analyze:
        return {emotion: None for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 400:
        return {emotion: None for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}

    if response.status_code != 200:
        raise Exception("Failed to get a valid response from the emotion detection API.")
    
    
    response_data = response.json()
    emotion_data = response_data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_data, key=emotion_data.get)

    return {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness'],
        'dominant_emotion': dominant_emotion
    }
