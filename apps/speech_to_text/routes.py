import os
from flask import jsonify, request
from werkzeug.utils import secure_filename
from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment
import wave

from . import speech_to_text
from ..text_to_braille.text_to_braille import textToBraille

# Google Cloud 설정
key_path = os.path.join(os.path.dirname(__file__), 'ringed-almanac-424316-v3-4155d32240f6.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

def convert_to_wav(file_path):
    audio_file = AudioSegment.from_file(file_path)
    wav_file = file_path.replace('.m4a', '.wav')
    audio_file = audio_file.set_channels(1)
    audio_file = audio_file.set_sample_width(2)
    audio_file.export(wav_file, format='wav')
    return wav_file

def get_sample_rate(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        return wav_file.getframerate()

def transcribe_audio(file_path):
    client = speech.SpeechClient()

    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    sample_rate = get_sample_rate(file_path)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code='ko-KR',
    )

    response = client.recognize(config=config, audio=audio)

    transcription = ""

    for result in response.results:
        transcription += result.alternatives[0].transcript
    
    return transcription

@speech_to_text.route("/", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400
    
    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(os.path.dirname(__file__), 'data')
        file_path = os.path.join(save_path, filename)
        file.save(os.path.join(file_path))

        try:
            if file_path.endswith('.m4a'):
                file_path = convert_to_wav(file_path)

            transcription = transcribe_audio(file_path)
            braille_list = textToBraille(transcription)
            ret = [{'word': transcription, 'braille': braille_list}]
            return jsonify(ret), 200
        finally:
            os.remove(os.path.join(save_path, filename))
            if file_path.endswith('.wav'):
                os.remove(file_path)