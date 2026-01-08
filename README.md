<<<<<<< HEAD
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
=======
# Healthcare IoT Monitoring - One-click Docker Compose (Windows/Docker Desktop)

Contents:
- docker-compose.yml        -> main stack (MariaDB, Zabbix server+web, agent, SNMP exporter, NETCONF poller, Grafana)
- prometheus/snmp.yml       -> snmp_exporter config
- netconf-poller/*          -> simple Python poller for NETCONF devices (example)
- grafana/provisioning/*    -> auto-provision Grafana datasource & dashboards
- zabbix/templates/*        -> minimal placeholder templates to import in Zabbix

Quick steps (Windows + Docker Desktop):
1. Ensure Docker Desktop is installed and WSL2 backend enabled OR use Docker Desktop Windows containers.
2. Open PowerShell in the folder where you extracted the project.
3. Run: `docker compose up -d`
4. Wait ~1-2 minutes for containers to initialize.
5. Access services:
   - Zabbix frontend: http://localhost:8080  (Login: Admin / zabbix)
   - Grafana: http://localhost:3000 (Login: admin / admin)
   - SNMP exporter metrics: http://localhost:9116/metrics
6. Import templates into Zabbix:
   - In Zabbix UI -> Configuration -> Templates -> Import the XML template files in `zabbix/templates/`.
   - Create hosts representing healthcare devices and link templates (SNMP template for SNMP devices, create host for NETCONF devices and match `zabbix_host` in netconf-poller/config.yml).
7. Alternative for step you couldn't do: If you couldn't complete "step 6" in a previous guide (likely WSL/permissions), you can run Docker Desktop with WSL2 integration, or run Docker Compose directly from PowerShell with administrative rights. If the problem was 'install plugin for Grafana' on Windows, the `GF_INSTALL_PLUGINS` env will install the Zabbix plugin at container start.
8. To stop: `docker compose down -v`

Notes & next steps:
- This repo provides a functional skeleton. For production-grade healthcare monitoring you must:
  - Harden DB and Zabbix credentials.
  - Configure SNMP community strings / versions per device.
  - Replace placeholder NETCONF RPCs with device-specific YANG paths.
  - Add Zabbix discovery rules, triggers, and escalation/notification actions.
  - Add TLS / network segmentation for patient-safety devices.

If you want, I can:
- Add a Prometheus + Alertmanager version.
- Add InfluxDB+Telegraf variant.
- Generate ready-to-import Zabbix templates for common medical device MIBs (if you provide MIB names).
>>>>>>> 01564bc (Initial commit: Healthcare monitoring system using Zabbix and Grafana)
