"""
Author: Hang Yan
Date created: 2023/8/9
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""

import os
import json
import openai


from .redis_conn import insert_system_prompt_if_not_exists, save_message, get_conversation_history
from config import HISTORY_SIZE, prompt_settings, PromptEnum

# Access the paragraph from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


openai.api_key = OPENAI_API_KEY
user_identifier = "Interviewer3"
conversation_key = f"conversation:{user_identifier}"


class GptHandler:
    def __init__(self):
        self.key = None
        self.sentence = ""
        # self.init_prompt(prompt_settings[PromptEnum.ChatGPT.value]["prompt"])

    def init_prompt(self, prompt_type, version=None):
        if prompt_type == PromptEnum.Dating.value:
            system_prompt = prompt_settings[prompt_type][version]["prompt"]
        else:
            system_prompt = prompt_settings[prompt_type]["prompt"]


        insert_system_prompt_if_not_exists(self.key, system_prompt)

    def generate_key_name(self, user, prompt_type):
        self.key = f"{user}{prompt_type}"


    def send_openai_request(self, messages):
        # # messages = [{'role': 'system', 'content': "Welcome to the Technical Interviewer chatbot! We're here to simulate a real technical interview for a Python developer position. The role requires expertise in Django, Redis, MySQL, and AWS. I'll be asking you questions to assess your skills. Let's make this experience as authentic as possible. We'll start with an introduction:"}, {'role': 'user', 'content': 'Yes'}, {'role': 'assistant', 'content': "Great! Let's start with a brief introduction. Please tell me about your background and experience as a Python developer."}, {'role': 'user', 'content': "I've been working about 5 years, and have responbile for full stack develpopment for many projects using Python, JS, Django, Tornado, FLask and db like Redis, MySQL"}, {'role': 'assistant', 'content': "That's impressive! It sounds like you have a solid background in Python development and have worked on a variety of projects using different frameworks and databases. In today's interview, we'll focus on your expertise in Django, Redis, MySQL, and AWS. Are you ready to get started with the questions?"}, {'role': 'user', 'content': 'ok'}, {'role': 'assistant', 'content': "Great! Let's begin with Django. \n\nQuestion 1: What is Django and what are some of its key features?"}]
        #
        # print(messages)
        # for k, v in messages:
        #     print(type(k), type(v))

        stream = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            temperature=0.4,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=messages,
            stream=True,
        )
        return stream

    def remove_duplicate_messages(self, conversation_history_list):
        # Process the conversation history and remove duplicate user messages
        unique_history = []
        for conversation_history in conversation_history_list:
            if conversation_history not in unique_history:
                unique_history.append(conversation_history)

        return unique_history

    def generate_response(self, user_prompt):
        messages = get_conversation_history(self.key, HISTORY_SIZE)
        user_prompt = {"role": "user", "content": user_prompt}
        save_message(self.key, user_prompt)
        messages.append(user_prompt)

        unique_history = self.remove_duplicate_messages(messages)
        return unique_history

    def get_conversation_history(self):
        # from ipdb import set_trace;
        # set_trace()
        messages = get_conversation_history(self.key, HISTORY_SIZE)
        if messages:
            unique_history = self.remove_duplicate_messages(messages)

        else:
            unique_history = list()
        return unique_history

if __name__ == "__main__":
    # system_prompt = "Welcome to the Technical Interviewer chatbot! We're here to simulate a real technical interview for a Python developer position. The role requires expertise in Django, Redis, MySQL, and AWS. I'll be asking you questions to assess your skills. Let's make this experience as authentic as possible. We'll start with an introduction:"
    system_prompt = "You are chat bot show me code"

    insert_system_prompt_if_not_exists(conversation_key, system_prompt)
    user_prompt = {"role": "user", "content": "Give me a Python code"}

