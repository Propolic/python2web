# print("Привет мир!")

from flask import Flask, json, request
import logging

import socket

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

@app.route('/')
def index():
    myIP = extraxt_ip()
    str = f'<p>Привет Матвейка! <br>Это наше первое приложение на Питоне в сети Интернет!<br>Ура!<br>{myIP}</p>'
    return str
