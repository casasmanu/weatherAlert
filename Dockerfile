FROM python:3
ENV TZ="Europe/Berlin"
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["python","main.py"]
