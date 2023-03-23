import unittest
from chatgpt_response2.gptresponseparser import jsonParser


class pilotResponseTest(unittest.TestCase):

    def test_to_get_command(self):

        response = "{\"id\":\"chatcmpl-6wy93Cf3ZNRPAE1u1EJtLfboIcJzr\", \"object\":\"chat.completion\", \"created\":1679512241, \"model\":\"gpt-3.5-turbo-0301\", \"usage\":{\"prompt_tokens\":15, \"completion_tokens\":41, \"total_tokens\":56}, \"choices\":[{\"message\":{\"role\":\"assistant\", \"content\":\"\\nIn Ruby, you can use the following code:\\n\\n```ruby\\nputs \\\"Hello, World!\\\"\\n```\\nThanks for using chatGPT.\"}, \"finish_reason\":\"stop\", \"index\":0}]}\n"

        responseTest = jsonParser(response)
        # print(responseTest)
        assert responseTest[0].startswith("puts")

    def test_to_get_info(self):
        pass
