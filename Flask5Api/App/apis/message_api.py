import json
from datetime import datetime

from flask import request, g
from flask_restful import Resource, abort, fields, marshal, reqparse
from geventwebsocket import WebSocketError

from App.apis.api_constant import HTTP_OK
from App.apis.model_utils import login_required
from App.models import Room, Message

parse_room_message = reqparse.RequestParser()
parse_room_message.add_argument("token", type=str, required=True, help="请输入令牌")
parse_room_message.add_argument("roomid", type=str, required=True, help="请输入房间id")
parse_room_message.add_argument("type", type=int)

message_fields = {
    "user_id": fields.Integer(attribute='message_author'),
    "from_user": fields.String,
    "roomid": fields.Integer(attribute='message_room'),
    "time": fields.String(attribute='timestamp'),
    "msg": fields.String(attribute='body'),
    "type": fields.Integer,
    "user_icon": fields.String,
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
        args = parse_room_message.parse_args()
        # user = g.user
        roomid = args.get("roomid")
        messages = Message.query.filter(Message.message_room == roomid)
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

        usr_socket = request.environ.get("wsgi.websocket")  # type:WebSocket

        # 查询用户的房间 并添加到通讯字典
        for room in user.rooms:
            if usr_socket:
                addtwodimdict(user_socket_dict, room.id, user.username, usr_socket)
                # 添加到通讯字典的同时，发送给该房间所有人上线信息
                for name, u_socket in user_socket_dict[room.id].items():
                    data = {
                        "status": HTTP_OK,
                        "num": len(user_socket_dict[room.id]),
                        "is_online": 1,
                        "username": user.username,
                        "roomid":room.id,
                        "type":0,
                    }
                    try:
                        u_socket.send(str(data))
                    except:
                        print(user_socket_dict)
                        del user_socket_dict[room.id][user.username]
                        print(user_socket_dict)
                        return

        # print(user_socket_dict)
        while True:
            try:
                msg = usr_socket.receive()
            except:
                for room in user.rooms:
                    del user_socket_dict[room.id][user.username]
                    for name, u_socket in user_socket_dict[room.id].items():
                        data = {
                            "status": HTTP_OK,
                            "num": len(user_socket_dict[room.id]),
                            "is_online": 0,
                            "username": user.username,
                        }
                        u_socket.send(str(data))
                break


            # break

            if msg is None:
                for room in user.rooms:
                    del user_socket_dict[room.id][user.username]
                    for name, u_socket in user_socket_dict[room.id].items():
                        data = {
                            "status": HTTP_OK,
                            "num": len(user_socket_dict[room.id]),
                            "is_online": 0,
                            "username": user.username,
                        }
                        u_socket.send(str(data))
                break

            if msg:
                print(msg)

                try:
                    msg = eval(msg)
                except:
                    break


                if msg.get("type") == 0:
                #登录
                    is_online = msg.get("is_online")
                #登出
                    if is_online == 0:
                        for room in user.rooms:
                            del user_socket_dict[room.id][user.username]
                            for name, u_socket in user_socket_dict[room.id].items():
                                data = {
                                    "status": HTTP_OK,
                                    "num": len(user_socket_dict[room.id]),
                                    "is_online": is_online,
                                    "username":user.username,
                                }
                                u_socket.send(str(data))

                    if is_online == 0:
                        break


                # 发送文字信息
                if msg.get("type") == 1:
                    message = Message()
                    message.body = msg.get('msg')
                    message.type = msg.get("type")

                    roomid = msg.get("roomid")
                    room = Room.query.get(roomid)
                    if room is None:
                        abort(400, msg="请提供正确的roomid")

                    message.message_author = user.id
                    message.message_room = room.id
                    message.from_user = user.username
                    message.user_icon = user.icon
                    # print(datetime.now())
                    message.timestamp = datetime.now()
                    message.save()

                    for name, u_socket in user_socket_dict[room.id].items():
                        try:

                            data = dict(marshal(message, message_fields))

                            u_socket.send(str(data))
                            # print("sended")

                        except WebSocketError as e:
                            print(user_socket_dict)
                            print(e)
                            del user_socket_dict[room.id][user.username]
                            break