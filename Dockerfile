FROM python:3
ENV TZ="Europe/Berlin"
WORKDIR /app
COPY . /app/
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]
