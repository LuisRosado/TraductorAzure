from flask import Flask, request, render_template
import requests, os, uuid
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')
LOCATION = os.getenv('LOCATION')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = ENDPOINT + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Ocp-Apim-Subscription-Region': LOCATION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]

    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )

if __name__ == '__main__':
    app.run(debug=True)
