from flask import Flask
import os
import sys
from chatgpt_response2 import gptService as service


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


app = Flask(__name__)
service_obj = service


@app.route("/ask/query/<query>")
def ask(query, service=service):
    response = list(service.ask(query))
    return response
