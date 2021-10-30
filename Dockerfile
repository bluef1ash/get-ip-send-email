FROM python:3.9-slim-buster
MAINTAINER bluef1ash liangtian_2005@163.com
ADD . /app
WORKDIR /app
ENV TZ=Asia/Shanghai
RUN apt-get -y update && apt-get -y install python3-pip && pip3 install pip --upgrade && pip install -r /app/requirements.txt && bash -c "touch /app/main.py"
ENTRYPOINT ["python", "-u", "/app/main.py"]
