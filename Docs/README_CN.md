# GPTBot
该项目基于Tornado框架构建，使用WebSocket实现实时的双向通信。它通过与GPT模型的交互，实现了文本生成的多个功能。

## 功能特点
- 语言翻译：能够进行实时的文本翻译，支持多种语言之间的互译。
- 文本摘要：能够生成长篇文章或段落的摘要或总结，帮助用户快速了解文本内容。
- 问题回答：具备智能问答的功能，可用于构建在线客服系统或知识库系统等，能够回答用户提出的问题。
- 对话生成：能够生成对话内容，可用于构建虚拟助手或聊天机器人等应用。


## 技术栈
GPTBot项目使用以下技术栈和工具：

- Python：主要编程语言
- Tornado：Web框架，用于构建基于WebSocket的实时应用程序。
- JavaScript：用于编写前端交互逻辑和实现WebSocket通信。
- HTML/CSS：用于构建项目的前端界面和样式。
- GPT模型：用于文本生成的核心模型。
- Docker：容器化平台，用于方便地构建、部署和运行应用程序。
- Redis：用于作为GPTBot应用程序的依赖项，提供缓存和数据存储功能。



## 安装和使用

以下是分别针对Docker，Docker Compose 和手动启动程序示例，其中 Docker 和手动启动需要本地安装和启动Redis。

### Docker 方式启动程序
```
docker build -t gptbot-app .
docker run -p 8000:8000 gptbot-app
```

### Docker Compose 方式启动程序
```
docker-compose up
```

### 手动启动

#### 依赖项安装
在使用GPTBot之前，需要安装项目的依赖项。可以使用以下命令安装所需的依赖项：

```
pip install -r requirements.txt

```


#### 启动
如果您不想使用Docker，也可以使用以下命令手动启动GPTBot：
```
python app.py
```

## Demo1
![Example Image](../static/images/demo.gif)

## Demo2
![Example Image](../static/images/demo2.gif)



# 版权和许可
GPTBot基于MIT许可证进行许可。详细信息请参阅许可文件。
如有任何问题或建议，请随时提出。感谢您的使用和贡献！