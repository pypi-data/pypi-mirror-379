"""
FreeClimb API

This is a manually implemented test to validate the
contents of https://github.com/FreeClimbAPI/Python-Getting-Started-Tutorial/blob/master/python-getting-started.py
are functioning as expected
"""

import unittest

import freeclimb
import json


class TestQuickStart(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPerclGeneration(self):
        message = "Hello, FreeClimb!"
        say = freeclimb.Say(text=message, privacy_mode=True)
        get_speech = freeclimb.GetSpeech(
            action_url="http://example.com/actionurl/getspeech",
            prompts=[say],
            grammar_file="grammar.xml",
        )
        record_utterance = freeclimb.RecordUtterance(
            action_url="http://example.actionurl/recordutterance",
            silence_timeout_ms=1000,
        )
        script = freeclimb.PerclScript(commands=[say, get_speech, record_utterance])
        data = script.to_json()
        print("GOT DATA")
        print(data)
        expected_json = json.dumps(
            [
                {"Say": {"text": "Hello, FreeClimb!", "loop": 1, "privacyMode": True}},
                {
                    "GetSpeech": {
                        "actionUrl": "http://example.com/actionurl/getspeech",
                        "grammarFile": "grammar.xml",
                        "prompts": [
                            {
                                "Say": {
                                    "text": "Hello, FreeClimb!",
                                    "loop": 1,
                                    "privacyMode": True,
                                }
                            }
                        ],
                    }
                },
                {
                    "RecordUtterance": {
                        "actionUrl": "http://example.actionurl/recordutterance",
                        "silenceTimeoutMs": 1000,
                    }
                },
            ]
        )
        self.maxDiff = None
        self.assertEqual(data, expected_json)


if __name__ == "__main__":
    unittest.main()
