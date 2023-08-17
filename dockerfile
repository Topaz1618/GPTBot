# 基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 拷贝项目文件到工作目录
COPY . /app

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝.env_dev和.env_pod文件到工作目录
COPY .env_dev /app/.env_dev
COPY .env_pod /app/.env_pod

# 安装并启动Redis服务
RUN apt-get update && apt-get install -y redis-server
RUN service redis-server start

# 暴露项目端口
EXPOSE 8000

# 启动应用程序
CMD ["python", "app.py"]