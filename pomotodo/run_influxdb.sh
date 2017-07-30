#! /bin/bash

docker run -d --name influxdb \
    -p 8086:8086 \
    -p 8083:8083 \
    -e INFLUXDB_ADMIN_ENABLED=true \
    -p 2003:2003 \
    -e INFLUXDB_GRAPHITE_ENABLED=true \
    -v `pwd`/influxdb:/var/lib/influxdb \
    influxdb:1.2.4
