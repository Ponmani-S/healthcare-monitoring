FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY netconf_poller.py .
COPY config.yml .
CMD ["python","netconf_poller.py"]
