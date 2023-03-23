import unittest
from unittest.mock import MagicMock
from chatgpt_response2.gptService import ask


class pilotServiceTest(unittest.TestCase):

    gptgateway = MagicMock()

    def test_service_call_gateway(self):

        query = "command to find files that start with xyz"

        response = ask(query, self.gptgateway)

        assert self.gptgateway.completion.iscalled
