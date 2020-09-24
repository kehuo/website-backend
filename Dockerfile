FROM kehuo/centos8_conda:v1 AS builder
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV PYTHONIOENCODING utf-8
ENV LANG en_US.UTF-8

WORKDIR /data/project

ADD ./ ./
RUN source ~/.bashrc \
    && conda activate myenv\
    && pip install --upgrade pip && pip install Cython && pip install path.py \
	&& pip install -r ./requirements.txt

CMD ["/root/miniconda3/envs/myenv/bin/python", "server.py"]
# docker run -itd -p 8050:5000 --name back backimg:v1

# FROM python:3.7-slim-buster
# WORKDIR /data/project
# ENV PYTHONIOENCODING utf-8
# ENV LANG en_US.UTF-8
#
# COPY . .
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt
# CMD [ "gunicorn", "ml:app", "-c", "./gunicorn.conf.py" ]