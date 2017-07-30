# -*- encoding: utf-8 -*-
import pprint
import requests
import datetime
from influxdb import InfluxDBClient

TODOS_API = "https://api.pomotodo.com/1/todos"
HAEDER = {
    "Authorization": "token crZ1lME6ctYMjACMAtw8N7Fmv8ZowYeM2QFq47wYjot7mmi2Rzo8NHT6bAlzw0K1a82AfSnrb1C4CuTKDpLS85QeuzH42ck9"
}


def get_todos():
    res = requests.get(TODOS_API, headers=HAEDER)
    data = res.json()
    list_data = list()
    for entry in data:
        single_data = {
            "measurement": "pomotodo",
            "tags": {
                "name": ""
            },
            "time": None,
            "fields": {
                "count": None
            }
        }
        if entry["description"] in [u'\u5b9e\u8df5', u'\u5b66\u4e60']:
            single_data["tags"]["name"] = entry["description"]
            single_data["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            single_data["fields"]["count"] = float(entry["costed_pomo_count"])
            list_data.append(single_data)

    client = InfluxDBClient(host='130.211.243.129', port=8086, database='pomotodo')
    client.write_points(list_data)


if __name__ == '__main__':
    get_todos()

