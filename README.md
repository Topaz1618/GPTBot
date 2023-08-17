# GPTBot

[中文README](/Docs/README.md)

GPTBot is a project built on the Tornado framework, utilizing WebSocket for real-time bidirectional communication. It enables various text generation capabilities by interacting with the GPT model.

## Features
- Language Translation: Enables real-time text translation, supporting translation between multiple languages.
- Text Summarization: Generates summaries or abstracts of long articles or paragraphs, helping users quickly grasp the content.
- Question Answering: Provides intelligent question-answering functionality, useful for building online customer support systems or knowledge base systems, capable of answering user queries.
- Dialogue Generation: Generates dialogue content, suitable for building virtual assistants or chatbots.

## Tech Stack
GPTBot utilizes the following technology stack and tools:

- Python: The primary programming language.
- Tornado: Web framework used for building WebSocket-based real-time applications.
- JavaScript: Used for writing frontend interaction logic and implementing WebSocket communication.
- HTML/CSS: Used for building the project's frontend interface and styling.
- GPT Model: The core model for text generation.
- Docker: Containerization platform used for convenient building, deployment, and running of the application.
- Redis: Used as a dependency for the GPTBot application, providing caching and data storage functionality.


## Installation and Usage

Below are examples for starting the program using Docker, Docker Compose, and manual startup methods. Note that Docker and manual startup require local installation and running of Redis.

### Docker Startup
```
docker build -t gptbot-app .
docker run -p 8000:8000 gptbot-app
```

### Docker Compose Startup
```
docker-compose up
```

### Manual Startup

#### Installing Dependencies
Before using GPTBot, ensure that the project's dependencies are installed. You can install the required dependencies using the following command:

```
pip install -r requirements.txt

```


#### Starting the Application
```
python app.py
```

## Demo1
![Example Image](/static/images/demo.gif)

## Demo2
![Example Image](/static/images/demo2.png)



# Copyright and License
GPTBot is licensed under the MIT License. Refer to the LICENSE file for more information.

Please feel free to ask any questions or provide suggestions. Thank you for using and contributing to GPTBot!