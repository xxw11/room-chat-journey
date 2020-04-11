import json

from flask import request, g
from flask_restful import Resource, abort, fields, marshal, reqparse
from geventwebsocket import WebSocketError

from App.apis.api_constant import HTTP_OK
from App.apis.model_utils import login_required
from App.models import Room, Message


parse_room_message=reqparse.RequestParser()
parse_room_message.add_argument("token", type=str, required=True, help="请输入令牌")
parse_room_message.add_argument("roomid",type=str, required=True, help="请输入房间id")
parse_room_message.add_argument("type",type=int)


message_fields = {
    "userid": fields.Integer(attribute='message_author'),
    "from_user": fields.String,
    "roomid": fields.Integer(attribute='message_room'),
    "time": fields.String(attribute='timestamp'),
    "msg": fields.String(attribute='body'),
    "type": fields.Integer,
    "user_icon":fields.String,
}
single_message_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(message_fields),
}

messages_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(message_fields)),
}

user_socket_list = []

user_socket_dict = {}


def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a: {key_b: val}})


class RoomMsgResource(Resource):
    @login_required
    def get(self):
        args=parse_room_message.parse_args()
        user = g.user
        roomid=args.get("roomid")
        messages=Message.query.filter(Message.message_room==roomid)
        data = {
            "status": HTTP_OK,
            "msg": "成功查询消息",
            "data": messages,
        }
        return marshal(data, messages_fields)


class MessageResource(Resource):
    @login_required
    def get(self):
        user = g.user
        room = request.args.get("room")
        type = request.args.get("type")
        # print(user.username, room)
        if not Room.query.get(room):
            abort(404, msg="无此房间")
        room = Room.query.get(room)
        usr_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
        # pprint.pprint(usr_socket)
        if usr_socket:
            addtwodimdict(user_socket_dict, room.id, user.username, usr_socket)
            # user_socket_dict[room][username]=usr_socket
            # print(len(user_socket_dict[room]), user_socket_dict)
        while True:
            try:
                msg = usr_socket.receive()
            except:
                continue

            if msg is None:
                user_socket_dict[room.id].pop(user.username)
                break
            if msg:

                message = Message()

                message.body = eval(msg).get('msg')
                message.message_author = user.id
                message.message_room = room.id
                message.from_user = user.username
                message.user_icon=user.icon
                message.type=type or 1

                message.save()

                for name,u_socket in user_socket_dict[room.id].items():
                    try:
                        # print(type(dict(marshal(data, message_fields))))
                        data=dict(marshal(message, message_fields))
                        # data["is_self"]=int(name==message.from_user)
                        u_socket.send( str(data) )
                    except WebSocketError as e:
                        print(user_socket_dict)
                        print(e)
                        user_socket_dict.pop(user.username)
