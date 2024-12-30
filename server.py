"""
Emotion Detector Server

This module sets up a Flask server to handle emotion detection requests.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def render_emotion_detector():
    """
    Endpoint to analyze emotions from the provided text.

    This function retrieves the text to be analyzed from the request
    parameters and uses the emotion_detector function to determine the 
    intensity of various emotions ('anger', 'disgust', 'fear', 'joy', 'sadness') 
    and the dominant emotion. If the dominant emotion cannot be determined, 
    an error message is returned.

    Returns:
        str: A message indicating the emotion analysis results or an error 
        message if the text is invalid.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # if dominant_emotion is None return message saying Invalid text! Please try again!
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""
        For the given statement, the system response is 
        'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 
        'joy': {joy} and 'sadness': {sadness}. 
        The dominant emotion is {dominant_emotion}.
    """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
