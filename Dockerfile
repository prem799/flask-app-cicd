FROM python:3.11.4-alpine3.17
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app
CMD ["flask", "run", "--host=0.0.0.0"]