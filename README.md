# GPTBot

[中文README](/Docs/README_CN.md)

GPTBot is a project built on the Tornado framework, utilizing WebSocket for real-time bidirectional communication. It enables various text generation capabilities by interacting with the GPT model.

## Features
- Language Translation: Enables real-time text translation, supporting translation between multiple languages.
- Text Summarization: Generates summaries or abstracts of long articles or paragraphs, helping users quickly grasp the content.
- Question Answering: Provides intelligent question-answering functionality, useful for building online customer support systems or knowledge base systems, capable of answering user queries.
- Dialogue Generation: Generates dialogue content, suitable for building virtual assistants or chatbots.

## Tech Stack
GPTBot utilizes the following technology stack and tools:

- Python
- JavaScript
- Tornado
- gpt-3.5 model: The core model for text generation
- Redis: Used as a dependency for the GPTBot to provide caching and data storage functionality.
- HTML/CSS
- Docker

## Installation and Usage

### Docker Compose Startup
```
docker-compose build
docker-compose up
```

### Manual Startup

#### Installing Dependencies
You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

#### Configure Redis Connection

Modify the following lines with your Redis host and port:

```
$ vim .env_prod
redis_host=your_redis_host
redis_port=your_redis_port
```

#### RUN
```
python app.py
```

## Example

### Input Box
![Example Image](/static/images/demo2.png)


### ChatBot
![Example Image](/static/images/demo.gif)



# Copyright and License
GPTBot is licensed under the [MIT License](LICENSE) License. Refer to the LICENSE file for more information.



Please feel free to ask any questions or provide suggestions. Thank you for using and contributing to GPTBot!