"""
Author: Hang Yan
Date created: 2023/8/9
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""



import os
import psutil
import re
import math
import uuid
import asyncio
from time import time, sleep

import tornado.ioloop
import tornado.web
import tornado.websocket

import os
import asyncio
import aiohttp
import psutil
from gpt_utils import GptHandler
from redis_conn import save_message


class IndexHandler(tornado.web.RequestHandler):
    async def get(self):
        self.render("test.html")


class ChatHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
        self.gpt = GptHandler()
        self.gpt.init_prompt()

    def on_message(self, message):
        # Process the message (e.g., call OpenAI API) and send the response back
        print("rece", message)
        conversation_history = self.gpt.generate_response(message)
        print(conversation_history)
        stream = self.gpt.send_openai_request(conversation_history)

        idx = 0
        for chunk in stream:
            # print(chunk)
            response = chunk["choices"][0]
            if response.get("finish_reason") == "stop":
                print("bye bye", self.gpt.sentence)
                save_message(self.gpt.key, {"role": "assistant", "content": self.gpt.sentence})
                self.write_message("END MSG")
                break

            role = response["delta"].get("role")
            content = response["delta"].get("content")
            if content:
                if idx == 0:
                    self.write_message("START MSG")
                print("content:", len(content), content)
                self.gpt.sentence += content
                self.write_message(content)
                idx += 1


#         l = """
#          user
#  authentication
#  and
#  access
#  control
# .
#
#
# 5
# .
#  Admin
#  interface
# :
#  Django
#  automatically
#  generates
#         """
#         idx = 0
#         for chunk in l :
#             print(chunk)
#             if idx == 0:
#                 self.write_message("start")
#
#             self.write_message(chunk)
#
#             idx += 1


    def on_close(self):
        print("WebSocket closed")


# 启动Tornado服务
if __name__ == '__main__':
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "login_url": "/login",
    }
    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/ws', ChatHandler),
    ],

        debug=True, **settings)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()