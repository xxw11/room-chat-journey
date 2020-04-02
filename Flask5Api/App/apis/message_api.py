import json

from flask import request, g
from flask_restful import Resource, abort
from geventwebsocket import WebSocketError

from App.apis.model_utils import login_required
from App.models import Room, Message

user_socket_list=[]

user_socket_dict={}

def addtwodimdict(thedict, key_a, key_b, val):
  if key_a in thedict:
    thedict[key_a].update({key_b: val})
  else:
    thedict.update({key_a:{key_b: val}})


class MessageResource(Resource):
    @login_required
    def get(self):
        user = g.user
        room=request.args.get("room")
        print(user.username, room)
        if not Room.query.get(room):
            abort(404,msg="无此房间")
        room=Room.query.get(room)
        usr_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
        # pprint.pprint(usr_socket)
        if usr_socket:
            addtwodimdict(user_socket_dict, room, user.username, usr_socket)
            # user_socket_dict[room][username]=usr_socket
            # print(len(user_socket_dict[room]), user_socket_dict)
        while True:
            msg = usr_socket.receive()
            message = Message()
            message.body = msg
            message.message_author=user.id
            message.message_room=room.id
            message.save()
            msg_dict = json.loads(msg)
            msg_dict["from_user"] = user.username
            msg_dict["room"] = room

            # to=msg_dict.get("to")
            # # msg_info=msg_dict.get("msg")
            # u_socket=user_socket_dict[room].get(to)
            # u_socket.send(json.dumps(msg_dict))

            for u_socket in user_socket_dict[room].values():
                print(u_socket)
                if u_socket == usr_socket:
                    continue
                try:
                    u_socket.send(json.dumps(msg_dict))
                except WebSocketError as e:
                    print(user_socket_dict)
                    print(e)
                    user_socket_dict.pop(user.username)