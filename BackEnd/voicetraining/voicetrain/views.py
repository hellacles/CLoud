from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse

import boto3
from google.cloud import speech
import os

from .modelPredict import start_predict
from .predictToText import predictToText

openApiURL = ""
accessKey = ""

@api_view(['GET'])
def index(request):
    print("get")
    return JsonResponse({'msg': 'hello'}, status=200)

@api_view(['POST'])
def SpeechToText(request):
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"] = ""
    # Instantiates a client
    client = speech.SpeechClient()

    s3 = boto3.resource('s3',
                   aws_access_key_id="",
                   aws_secret_access_key="",
                   region_name="")
    print("STT 분석을 시작합니다")
    obj = s3.Object('dev01e549a594b045b5897a771c14760e23141204-dev', 'public/recording.wav')
    audioFilePath = obj.get()['Body'].read()
    print("파일 가져오기 완료")

    content = audioFilePath
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,

        ##음성파일 hertz
        sample_rate_hertz=22050,
        language_code="ko-KR",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        pass

    print("요청 : " + result.alternatives[0].transcript)
    answer, orderNum = start_predict(result.alternatives[0].transcript)
    print("분석 끝")
    intentNum, res, shopname, destination, fromaddress, fromlatitude, fromlongitude, deslatitude, deslongitude, receipt = predictToText(answer, request.data['user'], orderNum)
    print("분석결과: ", res)
    return JsonResponse({'statusCode': '200', 'intentNum': intentNum, 'body': res, 'shopname': shopname, 'destination': destination, \
                         'fromaddress': fromaddress, 'fromlatitude': fromlatitude, 'fromlongitude': fromlongitude, 'deslatitude': deslatitude, \
                         'deslongitude': deslongitude, 'receipt': receipt}, status=200)

def detect_intent_texts(project_id, session_id, texts, language_code):
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    # for text in texts:
    text_input = dialogflow.types.TextInput(
        text=texts, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))

    return response.query_result.fulfillment_text