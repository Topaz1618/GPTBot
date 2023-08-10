import os
import json

import openai
from dotenv import load_dotenv

from redis_conn import save_message, get_conversation_history

# Load environment variables from .env file
load_dotenv()

# Access the paragraph from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HISTORY_SIZE = int(os.getenv("HISTORY_SIZE"))

# openai.api_key = "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"
system_prompt = "You are a good partner"
user_identifier = "User1"
conversation_key = f"conversation:{user_identifier}"


class PersonalAssistant(object):
    def __init__(self, topic_type=0, system_prompt=None):
        self.topic_type = topic_type
        self.system_prompt = system_prompt

    def send_openai_request(self, messages):
        stream = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            temperature=0.4,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=messages,
            stream=True,
        )

        """
        {
              "choices": [
                {
                  "delta": {
                    "content": " after"
                  },
                  "finish_reason": null,
                  "index": 0
                }
              ],
              "created": 1681908663,
              "id": "chatcmpl-771Z1v1xCDzg1FvFU1EELVTYTjSh4",
              "model": "gpt-3.5-turbo-0301",
              "object": "chat.completion.chunk"
            }
        """
        str = ""
        for chunk in stream:
            # print(chunk)
            response = chunk["choices"][0]
            if response.get("finish_reason") == "stop":
                print("bye bye")
                break

            role = response["delta"].get("role")
            content = response["delta"].get("content")
            if content:
                print(content)
                str += content

        print("gonna return")
        return str

    def generate_response(self, user_prompt):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt},
            # {"role": "assistant", "content": assistant_prompt},
            # {"role": "user", "content": user_prompt2},
            # {"role": "assistant", "content": "further answer"},
            # {"role": "user", "content": "further questions"},
        ]
        print(user_identifier)
        messages = get_conversation_history(user_identifier, HISTORY_SIZE)
        print(messages)

        # message = self.send_openai_request(messages)
        # print(message)
        # return message


if __name__ == "__main__":
    user_prompt = """ I love you """
    assistant = PersonalAssistant()
    # assistant.generate_realtime_response(user_prompt2)
    assistant.generate_response(user_prompt)
