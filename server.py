"""
Server using flask
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Take the emotion from a GET argument and detect emotions
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return f"""
    For the given statement, the system response is anger: {anger_score},
    disgust: {disgust_score},
    fear: {fear_score},
    joy: {joy_score},
    sadness: {sadness_score}. 
    The dominant emotion is {dominant_emotion}.
    """

@app.route("/")
def render_index_page():
    """
    Render the index main page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
