from urllib.request import urlopen, Request
import json
import time
from datetime import datetime

WRITE_FREQUENCY_SECONDS=30
PRINTER_NAME="cncEnder5"

MOONRAKER_API_URL='http://localhost:7125/printer/objects/query?extruder=target,temperature&heater_bed=target,temperature'

INFLUXDB_API_URL='http://192.168.1.2:28086/api/v2/write?org=quikstorm&bucket=moonraker'
INFLUXDB_API_TOKEN='OqtYbutFiezxLjnW0egCtb-AKyzcz6yhq_it5SkvgKQvwYoXwkr5aa_oyM8o3uitqEnCnZ9xdv01BPdgi2ciSw=='

def get_status():

    with urlopen(MOONRAKER_API_URL) as response:
        if response.status != 200:
            print("[{}] MOONRAKER ERROR: {} {}".format(datetime.now().isoformat(), status, response.read()))
            return

        body = response.read()

    data = json.loads(body)

    influx_lp="status,printer_name={} extruder_target={},extruder_temperature={},heater_bed_target={},heater_bed_temperature={}".format(
        PRINTER_NAME,
        data['result']['status']['extruder']['target'],
        data['result']['status']['extruder']['temperature'],
        data['result']['status']['heater_bed']['target'],
        data['result']['status']['heater_bed']['temperature']
        )

    print("[{}] {}".format(datetime.now().isoformat(), influx_lp))

    influx_request = Request(INFLUXDB_API_URL, headers={ 'Authorization':'Token ' + INFLUXDB_API_TOKEN, 'Content-Type': 'text/plain; charset=utf-8', 'Accept':'application/json'}, data=influx_lp.encode('utf-8'), method="POST")

    with urlopen(influx_request) as response:
        status = response.status
        if status < 200 or status > 299:
            print("[{}] ERR: {}".format(datetime.now().isoformat(), status))
        else:
            print("[{}] OK".format(datetime.now().isoformat()))


print("[{}] moonraker-influxdb-bridge started".format(datetime.now().isoformat()))
while(True):
    get_status()
    time.sleep(WRITE_FREQUENCY_SECONDS)

# end while

