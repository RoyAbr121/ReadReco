FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7001

CMD ["python", "run.py"]