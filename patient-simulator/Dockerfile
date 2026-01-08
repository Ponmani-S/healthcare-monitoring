FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y zabbix-sender

RUN pip install requests pyzabbix

COPY patient_simulator.py .

CMD ["python", "patient_simulator.py"]
