FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip
ADD ./statistics/src/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/src/protos
ADD ./statistics/src /app
ADD ./common/ /app/common


EXPOSE 1329
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1329"]