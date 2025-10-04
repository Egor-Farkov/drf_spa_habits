FROM python:3.11-slim
WORKDIR /drf_spa_habits
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
