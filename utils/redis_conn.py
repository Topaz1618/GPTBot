"""
Author: Hang Yan
Date created: 2023/8/9
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.

"""


import json
import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def insert_system_prompt_if_not_exists(conversation_key, system_prompt):
    # Check if the system prompt already exists in the Redis List
    if not redis_client.lrange(conversation_key, 0, -1) or json.loads(redis_client.lindex(conversation_key, 0))['role'] != 'system':
        # Insert the system prompt at the beginning of the Redis List
        redis_client.lpush(conversation_key, json.dumps({"role": "system", "content": system_prompt}))


def save_message(conversation_key, message):
    # Save the new message to the Redis List
    redis_client.rpush(conversation_key, json.dumps(message))


def insert_message(conversation_key, message):
    # Save the new message to the Redis List
    redis_client.lpush(conversation_key, json.dumps(message))

def get_conversation_history(conversation_key, count):
    # Retrieve the entire conversation history from the Redis List
    history = redis_client.lrange(conversation_key, 0, count - 1)
    return [json.loads(message) for message in history]


def update_latest_question(conversation_key, user_question, assistant_response):
    # Update the Redis Hash with the latest user question and assistant response
    redis_client.hset(conversation_key, "user_question", json.dumps(user_question))
    redis_client.hset(conversation_key, "assistant_response", json.dumps(assistant_response))


if __name__ == "__main__":
    # Example conversation key (use the user's identifier)
    user_identifier = "User2"
    conversation_key = f"conversation:{user_identifier}"

    # Sample messages
    system_message = {"role": "system", "content": "You are a best partner can show love."}
    user_message = {"role": "user", "content": "How've you been"}
    assistant_message = {"role": "assistant", "content": "All good"}

    # Save user and assistant messages
    insert_message(conversation_key, system_message)
    save_message(conversation_key, user_message)
    save_message(conversation_key, assistant_message)

    # Retrieve conversation history
    conversation_history = get_conversation_history(conversation_key, 20)
    # for message in conversation_history:
    #     print(f"{message['role']}: {message['content']}")

    print(conversation_key, conversation_history)

    # Update latest user question and assistant response
    # update_latest_question(conversation_key, user_message, assistant_message)
    # latest_user_question = json.loads(redis_client.hget(conversation_key, "user_question"))
    # latest_assistant_response = json.loads(redis_client.hget(conversation_key, "assistant_response"))

    # print("\nLatest User Question:", latest_user_question['content'])
    # print("Latest Assistant Response:", latest_assistant_response['content'])
