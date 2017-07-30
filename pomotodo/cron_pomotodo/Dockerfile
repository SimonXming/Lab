FROM python:3.5-alpine
MAINTAINER simonshyu

ENV CODE_BASE /code

COPY cron_pomotodo.py /code/cron_pomotodo.py
COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir


CMD ["python", "/code/cron_pomotodo.py"]