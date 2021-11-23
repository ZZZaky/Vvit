from flask import Flask, render_template, request
import requests
import os
import uuid
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        original_text = request.form['text']
        target_language = request.form['language']

        key = os.environ['KEY']
        endpoint = os.environ['ENDPOINT']
        location = os.environ['LOCATION']

        path = '/translate?api-version=3.0'

        target_language_parameter = '&to=' + target_language

        constructed_url = endpoint + path + target_language_parameter

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{ 'text': original_text }]

        translator_request = requests.post(
            constructed_url, headers=headers, json = body)

        translator_response = translator_request.json()

        translated_text = translator_response[0]['translations'][0]['text']

        return render_template(
            'results.html',
            translated_text=translated_text,
            original_text=original_text,
            target_language=target_language
        )