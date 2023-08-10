import os
import json
from dotenv import load_dotenv

import openai
# from SuperTalkAI.settings import OPENAI_API_KEY

from public_info import PublicInfo

# Load environment variables from .env file
load_dotenv()

# Access the paragraph from the environment variable
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# print(pOPENAI_API_KEYar)


openai.api_key = OPENAI_API_KEY


class PersonalAssistant(object):
    def __init__(self, topic_type=0, country_code=None, ip_address=None):
        self.topic_type = topic_type
        self.country_code = country_code
        self.ip_address = ip_address

        # self.system_prompt = generate_system_prompt(topic_type)
        self.system_prompt = "You are a robot answer all the questions"

        self.check_public_ip()

    def __str__(self):
        return f"PersonalAssistant(country_code={self.country_code}, ip_address={self.ip_address})"

    def __repr__(self):
        repr_str = f"PersonalAssistant(topic_type={self.topic_type}"
        if self.country_code is not None:
            repr_str += f", country_code={self.country_code}"

        if self.ip_address is not None:
            repr_str += f", ip_address={self.ip_address}"

        repr_str += ")"
        return repr_str

    def check_public_ip(self):
        self.country_code, self.ip_address = PublicInfo().get_public_ip()
        print("Public IP address: ", self.ip_address)
        if self.country_code != "US":
            print("Check the Ip Address")
            return

    def get_country_code(self):
        return self.country_code

    def get_ip_address(self):
        return self.ip_address

    def send_openai_request(self, messages):
        stream = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
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
        message = self.send_openai_request(messages)
        print(message)
        # return message


if __name__ == "__main__":
    user_prompt = """ what's this ?  cognitive shortcuts or heuristics """
    assistant = PersonalAssistant()
    # assistant.generate_realtime_response(user_prompt2)
    assistant.generate_response(user_prompt)
