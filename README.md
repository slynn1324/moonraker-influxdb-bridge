# moonraker-influxdb-bridge

a simple python script that polls moonraker for temperatures and reports them to influxdb.

moonraker has mqtt integration, but it publishes every 250ms with no way to reduce the frequency (and in turn the granularity stored in influx)
