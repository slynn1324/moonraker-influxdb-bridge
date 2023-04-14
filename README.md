# moonraker-influxdb-bridge

a simple python script that polls moonraker for temperatures and reports them to influxdb.

moonraker has mqtt integration, but it publishes every 250ms with no way to reduce the frequency (and in turn the granularity stored in influx)

## setup

change the parameters at the top of mib.py to fit your environment

build the container with `./build.sh`

run the container with `./run.sh`

