#! /bin/bash

docker run -i -d --name grafana \
    -p 3000:3000 \
    -v `pwd`/grafana:/var/lib/grafana \
    -e GF_SECURITY_ADMIN_PASSWORD=admin \
    grafana/grafana:latest
