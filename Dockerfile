FROM python:3.9-alpine
LABEL MAINTAINER="bluef1ash liangtian_2005@163.com"
COPY . /app
WORKDIR /app
ENV TZ=Asia/Shanghai
RUN apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && pip install --no-cache-dir -r /app/requirements.txt
ENTRYPOINT ["python", "-u", "/app/main.py"]
