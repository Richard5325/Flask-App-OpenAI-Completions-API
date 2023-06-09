import unittest
from unittest.mock import MagicMock

from chatgpt_response2.gptcontroller import ask


class responseControllerShould(unittest.TestCase):
    service = MagicMock()
    #controller = Controller(service)

    def test_controller_should_call_the_service(self):
        query = "command to find files that start with xyz"
        # set_service(self.service)
        response = ask(query, self.service)

        assert self.service.ask.iscalled
