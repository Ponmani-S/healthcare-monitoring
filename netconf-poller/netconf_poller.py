#!/usr/bin/env python3
# Simple NETCONF poller that reads devices from config.yml and sends a numeric item via Zabbix sender API.
import yaml, time, logging
from ncclient import manager
from zabbix_api import ZabbixAPI

logging.basicConfig(level=logging.INFO)

with open('config.yml') as f:
    cfg = yaml.safe_load(f)

zbx = ZabbixAPI(server=cfg.get('zabbix_api','http://zabbix-server:8080'))
zbx.login(cfg.get('zabbix_user','Admin'), cfg.get('zabbix_password','zabbix'))

def poll_device(dev):
    try:
        logging.info(f"Connecting to NETCONF device {dev['host']}")
        with manager.connect(host=dev['host'], port=dev.get('port',830),
                             username=dev['username'], password=dev['password'],
                             hostkey_verify=False, allow_agent=False, look_for_keys=False) as m:
            # this is a placeholder <get> - adapt to your device/YANG
            result = m.get(filter=('subtree', '<system-state/>'))
            # stub: convert result to a metric
            metric_value = len(str(result))
            logging.info(f"Got value {metric_value} from {dev['host']}")
            # send to Zabbix via API as a trapper item (requires pre-created host and item)
            # Here we find host and send value using zabbix API: create/update item or use zabbix_sender if available
            hosts = zbx.host.get(filter={'host': dev['zabbix_host']})
            if hosts:
                hostid = hosts[0]['hostid']
                # send item via zabbix.history? Simpler: use zabbix API to create an item value
                # For full implementation, use zabbix_sender. For now, log output.
                logging.info(f"Would push {metric_value} to Zabbix host {dev['zabbix_host']} (hostid {hostid})")
    except Exception as e:
        logging.exception("Poll failed: %s", e)

if __name__ == '__main__':
    devices = cfg.get('devices',[])
    interval = cfg.get('interval',60)
    while True:
        for d in devices:
            poll_device(d)
        time.sleep(interval)
