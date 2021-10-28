FROM python:3.9-slim-buster
MAINTAINER bluef1ash liangtian_2005@163.com
ADD . /app
WORKDIR /app
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' > /etc/timezone
ENV TZ=Asia/Shanghai
RUN apt-get update -y && apt-get install -y python3-pip
RUN pip3 install pip --upgrade
RUN pip install -r /app/requirements.txt
RUN bash -c "touch /app/main.py"
ENTRYPOINT ["python", "-u", "/app/main.py"]
