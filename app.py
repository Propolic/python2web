# print("Привет мир!")

from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Привет Матвейка! <br>Это наше первое приложение на Питоне в сети Интернет!<br>Ура!</p>"
