# -*- encoding: utf-8 -*-
import logging
import requests
import datetime
import tornado.web
import tornado.ioloop
from tornado.web import url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado.gen import Return, coroutine
from influxdb import InfluxDBClient


DB_HOST = "127.0.0.1"
DB_PORT = 8086
DB_USER = ""
DB_PASSWORD = ""
DB_NAME = "pomotodo"

TODOS_API = "https://api.pomotodo.com/1/todos"
HAEDER = {
    "Authorization": "token"
}


class TestHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT")

    def get(self):
        get_todos()
        self.write("Success!")
        self.finish()

url_patterns = [
    url(r"/?", TestHandler, name="TestHandler")
]


class Application(tornado.web.Application):
    def __init__(self, config):
        _handlers = url_patterns
        settings = dict()
        self.client = InfluxDBClient(host=DB_HOST, port=DB_PORT, database=DB_NAME)
        super(Application, self).__init__(
            handlers=_handlers,
            **settings
        )

        corn_task = tornado.ioloop.PeriodicCallback(
            self.update_todos_to_influxdb,
            5 * 1000
        )
        corn_task.start()

    def update_todos_to_influxdb(self):
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
        self.client.write_points(list_data)


def main():
    config = {
        "host": "localhost",
        "port": 10080
    }
    options.logging = 'debug'
    tornado.log.enable_pretty_logging()

    application = Application(config)
    http_server = HTTPServer(application)
    http_server.listen(
        config["port"],
        address=config["host"]
    )

    logging.debug('Server listened on {}:{}'.format(
        config["host"],
        config["port"],)
    )

    IOLoop.current().start()

if __name__ == '__main__':
    main()
