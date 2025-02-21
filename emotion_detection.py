import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    dominant_emotion = 'anger'
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    if (disgust_score > anger_score): dominant_emotion = 'disgust'
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    if (fear_score > disgust_score): dominant_emotion = 'fear'
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    if (joy_score > fear_score): dominant_emotion = 'joy'
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    if (sadness_score > joy_score): dominant_emotion = 'sadness'

    



    # Returning a dictionary containing sentiment analysis results
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }