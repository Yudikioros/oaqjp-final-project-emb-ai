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

    if(response.status_code == 400):
      return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }  

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    dominant_emotion = 'anger'
    dominant_score = anger_score
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    if (disgust_score > dominant_score): 
        dominant_emotion = 'disgust'
        dominant_score = disgust_score
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    if (fear_score > dominant_score): 
        dominant_emotion = 'fear'
        dominant_score = fear_score
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    if (joy_score > dominant_score): 
        dominant_emotion = 'joy'
        dominant_score = joy_score
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    if (sadness_score > dominant_score): 
        dominant_emotion = 'sadness'
        dominant_score = sadness_score

    # Returning a dictionary containing sentiment analysis results
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }