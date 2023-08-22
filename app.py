from flask import Flask, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    r = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        return text

if __name__ == '__main__':
    app.run(debug="true",host="0.0.0.0",port=8080)
