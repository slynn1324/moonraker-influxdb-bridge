#!/bin/sh

podman run -d --name "moonraker-influxdb-bridge" --net=host --restart=unless-stopped moonraker-influxdb-bridge
