import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes the given text to detect emotions and returns the intensity of 
    each emotion along with the dominant emotion.

    Parameters:
    text_to_analyse (str): The text to be analyzed for emotions.

    Returns:
    dict: A dictionary containing the intensity of emotions ('anger', 
    'disgust', 'fear', 'joy', 'sadness') and the 'dominant_emotion'.
    """

    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    emotion=formatted_response['emotionPredictions'][0]['emotion']

    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    # Get which emotion is dominant and return the name of the emotion
    dominant_emotion = max(emotion, key=emotion.get)
    
    # return response
    return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }