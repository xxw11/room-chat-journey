import json
from datetime import datetime

from flask import request, g
from flask_restful import Resource, abort, fields, marshal, reqparse
from geventwebsocket import WebSocketError
from werkzeug.utils import secure_filename

from App.apis.api_constant import HTTP_OK
from App.apis.model_utils import login_required, change_filename
from App.models import Room, Message
from App.settings import PIC_DIR, FILE_DIR

parse_room_message = reqparse.RequestParser()
parse_room_message.add_argument("token", type=str, required=True, help="请输入令牌")
parse_room_message.add_argument("roomid", type=int, required=True, help="请输入房间id")
parse_room_message.add_argument("search_type", type=int)
parse_room_message.add_argument("search_info", type=str)

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

class RoomSearchResource(Resource):
    @login_required
    def get(self):
        args = parse_room_message.parse_args()
        user = g.user
        search_info=args.get("search_info")or ""
        search_type = args.get("search_type") or 1
        roomid = args.get("roomid")
        room=Room.query.get(roomid)

        print(args.get("search_info"))

        if (not room) or not(user in room.users):
            abort(400,msg="illegal!")
        messages = Message.query.filter(
            Message.body.ilike('%' + search_info + '%')).filter(
            Message.type==search_type
        ).filter(
            Message.message_room==room.id
        )

        data = {
            "status": HTTP_OK,
            "msg": "成功查询消息",
            "data": messages,
        }
        return marshal(data, messages_fields)


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


class MsgPictureResource(Resource):
    @login_required
    def post(self):
        user=g.user
        args = parse_room_message.parse_args()

        roomid = args.get("roomid")
        room=Room.query.get(roomid)
        if room is None:
            abort(404, msg="room don't exit")

        picture = request.files.get("picture")
        if picture is None:
            abort(404, msg="请上传图片")
        try:
            picture.filename = secure_filename(picture.filename)
            picture.filename = change_filename(picture.filename)
            picture.filename = str(user.id) + picture.filename
            filepath = PIC_DIR + picture.filename
            picture.save(filepath)
        except:
            abort(401,"图片上传失败")
        message = Message()
        message.body = "http://39.106.119.191/uploads/pictures/"+picture.filename
        message.type = 2
        message.message_author = user.id
        message.message_room = roomid
        message.from_user = user.username
        message.user_icon = user.icon
        message.timestamp = datetime.now()
        message.save()

        for name, u_socket in user_socket_dict[roomid].items():
            try:
                data = dict(marshal(message, message_fields))
                u_socket.send(str(data))
            except Exception:
                pass

class MsgFileResource(Resource):
    @login_required
    def post(self):
        user=g.user
        args = parse_room_message.parse_args()

        roomid = args.get("roomid")
        room = Room.query.get(roomid)
        if room is None:
            abort(404, msg="room don't exit")

        picture = request.files.get("file")
        if picture is None:
            abort(404, msg="请上传文件")
        try:
            picture.filename = secure_filename(picture.filename)
            picture.filename = change_filename(picture.filename)
            picture.filename = str(user.id) + picture.filename
            filepath = FILE_DIR + picture.filename
            picture.save(filepath)
        except:
            abort(401,"文件上传失败")
        message = Message()
        message.body = "http://39.106.119.191/uploads/files/"+picture.filename
        message.type = 3
        message.message_author = user.id
        message.message_room = roomid
        message.from_user = user.username
        message.user_icon = user.icon
        message.timestamp = datetime.now()
        message.save()

        for name, u_socket in user_socket_dict[roomid].items():
            try:
                data = dict(marshal(message, message_fields))
                u_socket.send(str(data))
            except Exception:
                pass

class MessageResource(Resource):
    @login_required
    def get(self):
        user = g.user
        # print(user.id)
        usr_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
        # print(usr_socket)
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
                    except WebSocketError as e:
                        print(user_socket_dict)
                        if user.username in user_socket_dict[room.id]:
                            del user_socket_dict[room.id][user.username]
                        print(e)
                        return

        # print(user_socket_dict)
        while True:
            try:
                msg = usr_socket.receive()
                print(msg)
            except:
                for room in user.rooms:
                    if user.username in user_socket_dict[room.id]:
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
                    if user.username in user_socket_dict[room.id]:
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
                # print(msg)

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
                            if user.username in user_socket_dict[room.id]:
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
                            if user.username in user_socket_dict[room.id]:
                                del user_socket_dict[room.id][user.username]
                            break


