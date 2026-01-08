import time
import random
import subprocess
from pyzabbix import ZabbixAPI

ZBX_SERVER = "hiz_zabbix_server"
ZBX_WEB = "http://hiz_zabbix_web:8080"

zbx = ZabbixAPI(ZBX_WEB)
zbx.login("Admin", "zabbix")

host = "PATIENT-01"

# Check if host exists
existing = zbx.host.get({"filter": {"host": host}})
if not existing:
    print("Creating host...")
    host_id = zbx.host.create({
        "host": host,
        "interfaces": [{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": "127.0.0.1",
            "dns": "",
            "port": "10050"
        }],
        "groups": [{"groupid": "2"}]
    })["hostids"][0]
else:
    host_id = existing[0]["hostid"]
    print("Host exists:", host_id)

# Define trapper items
items = {
    "heart_rate": "Heart Rate",
    "oxygen": "Oxygen Saturation",
    "temperature": "Body Temperature",
    "bp_systolic": "BP Systolic",
    "bp_diastolic": "BP Diastolic",
    "resp_rate": "Respiration Rate"
}

# Create item if needed
for key, name in items.items():
    chk = zbx.item.get({"hostids": host_id, "search": {"key_": key}})
    if not chk:
        print("Creating item:", key)
        zbx.item.create({
            "name": name,
            "key_": key,
            "hostid": host_id,
            "type": 2,         # trapper
            "value_type": 0
        })

print("Starting data simulation...")

# SMTP Password: qwyh rjfk ujai xphr
# MAIN LOOP
while True:
    data = {
        "heart_rate": random.randint(60, 100),
        "oxygen": random.randint(92, 100),
        "temperature": round(random.uniform(36.5, 38.5), 2),
        "bp_systolic": random.randint(110, 140),
        "bp_diastolic": random.randint(70, 90),
        "resp_rate": random.randint(12, 22)
    }

    for key, val in data.items():
        print(f"Sending -> {key} = {val}")
        subprocess.run([
            "zabbix_sender",
            "-z", ZBX_SERVER,
            "-s", host,
            "-k", key,
            "-o", str(val)
        ])

    time.sleep(10)

#docker cp C:\zabbix-stack\grafana.ini hiz_grafana:/etc/grafana/grafana.ini
#docker restart hiz_grafana
#docker compose up -d