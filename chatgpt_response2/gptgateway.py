import os
import sys
from pprint import pprint
import requests
import json
from chatgpt_response2 import gptresponseparser

CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


def completion(requestData):

    api_key = os.getenv('CHATGPT_API_KEY')
    endpoint = "https://api.openai.com/v1/chat/completions"

    headers = {"Authorization": f"Bearer {api_key}",
               "Content-Type": "application/json"}
    response = requests.post(endpoint, json=requestData, headers=headers)

    return gptresponseparser.jsonParser(response.text)
