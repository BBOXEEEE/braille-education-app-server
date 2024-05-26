from flask import Flask
from flask_cors import CORS
from apps.object_detection import object_detection
from apps.speech_to_text import speech_to_text

app = Flask(__name__)
CORS(app)

app.register_blueprint(object_detection, url_prefix='/')
app.register_blueprint(speech_to_text, url_prefix='/stt')


address = '0.0.0.0'
port = 15555

if __name__ == '__main__':
    app.run(debug=True, host=address, port=port)