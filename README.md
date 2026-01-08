#Healthcare Monitoring System using Zabbix, Grafana & Docker

#Project Overview

This project implements a real-time healthcare monitoring system using simulated patient vital data. Dummy health parameters are generated at regular intervals to mimic real medical sensors and are monitored using Zabbix and Grafana, with alerting mechanisms for abnormal conditions. The system demonstrates how modern hospitals and remote health-care platforms can continuously monitor patient vitals, visualize trends, and trigger alerts for timely intervention.

#Objectives

To simulate real-time patient health data using dummy values
To monitor patient vitals using an industry-grade monitoring stack
To visualize live and historical health data
To configure automated alerts for abnormal conditions
To build a modular, scalable, and containerized healthcare monitoring architecture

#Key Features

Real-time data updates every 5 seconds
Interactive dashboards using Grafana
Alerting for abnormal vitals (Temperature, Heart Rate, etc.)
Fully containerized using Docker & Docker Compose
Persistent storage using databases
API-based integration between services
Historical data analysis and trend visualization

#System Architecture

Patient Simulator (Dummy Data)
        ↓
   Zabbix Agent
        ↓
   Zabbix Server
        ↓
     Database
        ↓
      Grafana
        ↓
 Alert Engine & Notifications

#How to Run the Project

Prerequisites: Docker Desktop, Docker Compose, Windows / Linux / macOS

Start the Project:
cd zabbix-stack
docker compose up -d

Stop the Project (Without Data Loss):
docker compose down

#Access URLs

Zabbix Web UI: http://localhost:8080
Grafana: http://localhost:3000

#Future Enhancements

Add ML-based anomaly detection
Integrate real medical sensors
Mobile app for doctors
SMS / WhatsApp alert notifications
Multi-hospital deployment
AI-based health prediction

#Conclusion

This project demonstrates a real-world healthcare monitoring architecture using modern DevOps and monitoring tools. It showcases how simulated health data can be collected, stored, visualized, and monitored with alerts—similar to production healthcare systems.

This project demonstrates a real-world healthcare monitoring architecture using modern DevOps and monitoring tools.
It showcases how simulated health data can be collected, stored, visualized, and monitored with alerts—similar to production healthcare systems.
