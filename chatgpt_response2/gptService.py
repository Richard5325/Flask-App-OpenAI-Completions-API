import os
import sys
import json
from chatgpt_response2 import gptgateway

CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)
gptgateway_Obj = gptgateway


def ask(query, gptgateway=gptgateway):
    requestData = json.loads("""
        {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": " """ + query + """ "}],
                "temperature": 0.3
                }
        """)

    response = gptgateway.completion(requestData)
    return response
