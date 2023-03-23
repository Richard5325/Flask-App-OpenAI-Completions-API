import flask
import flask_unittest

from chatgpt_response2.gptcontroller import app


class codePilotTest(flask_unittest.ClientTestCase):

    app = app

    def test_when_queried_responds_back_with_command(self, client):
        query = "command to find files that start with xyz"

        response = client.get("/ask/query/" + query)
        res = response.text.strip('][').split(',')

        assert res[0].startswith("\"find")

    def test_when_queried_responds_back_with_info(self, client):

        query = "command to find files that start with xyz"

        response = client.get("/ask/query/" + query)
        res = response.text.strip('][').split(',')

        assert res[1] != None
