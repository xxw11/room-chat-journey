import json
import os
import pprint

from flask import render_template, url_for, request
from flask_migrate import MigrateCommand
from flask_script import Manager
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer


from App import create_app


env = os.environ.get("FLASK_ENV", "develop")

app = create_app(env)


manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # manager.run()

    http_serv = WSGIServer(("127.0.0.1",5000),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()