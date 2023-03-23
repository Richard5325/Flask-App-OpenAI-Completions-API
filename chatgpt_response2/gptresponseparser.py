import os
import sys
import json


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


def __init__(self):
    self.parsedResponse = None


def set_response(self, response):
    self.response = response


def get_content(parsedResponse):
    return parsedResponse["choices"][0]["message"]["content"]


def get_command(parsedResponse):

    command_enclosed = 0
    command = None
    content = get_content(parsedResponse)
    for line in content.split("\n"):
        if command_enclosed == 1:
            command = line.strip()
            break
        else:
            if line.startswith("```"):
                command_enclosed = command_enclosed+1

    return command


def get_info(parsedResponse):
    content = get_content(parsedResponse)
    info = content[content.rindex("`") + 1:].strip()
    return info


def jsonParser(response):
    parsedResponse = json.loads(response)
    command = get_command(parsedResponse)
    info = get_info(parsedResponse)
    return [command, info]
