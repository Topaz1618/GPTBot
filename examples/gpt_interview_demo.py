"""
Author: Hang Yan
Date created: 2023/8/9
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""

import os
import json
import openai

from dotenv import load_dotenv
from redis_conn import insert_system_prompt_if_not_exists, save_message, get_conversation_history
from config import SYSTEM_PROMPT

load_dotenv("../.env_dev")

# Access the paragraph from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HISTORY_SIZE = 30

openai.api_key = OPENAI_API_KEY
# proxy_host = '127.0.0.1'
# proxy_port = '33210'
# proxy_url = f'https://{proxy_host}:{proxy_port}'
# os.environ['HTTPS_PROXY'] = proxy_url

user_identifier = "Interviewer2"
conversation_key = f"conversation:{user_identifier}"


class PersonalAssistant(object):
    def __init__(self, topic_type=0):
        self.topic_type = topic_type

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


    def remove_duplicate_messages(self, conversation_history_list):
        # Process the conversation history and remove duplicate user messages
        unique_history = []
        for conversation_history in conversation_history_list:
            if conversation_history not in unique_history:
                unique_history.append(conversation_history)

        return unique_history

    def generate_response(self, user_prompt):
        messages = get_conversation_history(conversation_key, HISTORY_SIZE)
        save_message(conversation_key, user_prompt)
        messages.append(user_prompt)

        unique_history = self.remove_duplicate_messages(messages)
        print(unique_history)

        assistant_message = self.send_openai_request(unique_history)
        print(assistant_message)


        assistant_msg = {"role": "assistant", "content": assistant_message}
        save_message(conversation_key, assistant_msg)


if __name__ == "__main__":
    system_prompt =  SYSTEM_PROMPT["Interview"]["prompt"]
    insert_system_prompt_if_not_exists(conversation_key, system_prompt)
    user_prompt = {"role": "user", "content": "ok"}
    assistant = PersonalAssistant()
    # assistant.generate_realtime_response(user_prompt2)
    assistant.generate_response(user_prompt)
