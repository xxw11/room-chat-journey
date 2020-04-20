import random

from flask import g, request
from flask_restful import Resource, fields, marshal, reqparse, abort
from werkzeug.utils import secure_filename

from App.apis.api_constant import HTTP_CREATE_OK, ROOM_ACTION_JOIN, ROOM_ACTION_REGISTER, HTTP_OK
from App.apis.model_utils import login_required, change_filename
from App.models import Room
from App.settings import ROOM_DIR

parse_room_post=reqparse.RequestParser()
parse_room_post.add_argument("name", type=str)
parse_room_post.add_argument("detail", type=str)
parse_room_post.add_argument("action", type=str, required=True, help="请输入请求参数")

parse_room_post_join=parse_room_post.copy()
parse_room_post_join.add_argument("roomid", type=int, required=True, help="请输入房间id")

parse_room_patch=reqparse.RequestParser()
parse_room_patch.add_argument("name", type=str)
parse_room_patch.add_argument("detail", type=str)
parse_room_patch.add_argument("roomid", type=int, required=True, help="请输入房间id")


room_fields={
    "id": fields.Integer,
    "host_id":fields.Integer,
    "url":fields.String,
    "name":fields.String,
    "icon":fields.String,
    "detail":fields.String,
}
single_room_fields={
    "status":fields.Integer,
    "msg":fields.String,
    "data":fields.Nested(room_fields),
}
rooms_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(room_fields)),
}





class RoomResource(Resource):

    @login_required
    def get(self):
        user =g.user
        data = {
            "status": HTTP_OK,
            "msg": "房间查询成功",
            "data": user.rooms,
        }

        return marshal(data,rooms_fields)


    @login_required
    def post(self):

        args=parse_room_post.parse_args()
        action=args.get("action").lower()
        user =g.user
        room = Room()

        if action==ROOM_ACTION_JOIN:
            args = parse_room_post_join.parse_args()
            roomid=args.get("roomid")
            if not Room.query.get(roomid):
                abort(404,msg="房间号不存在")
            room=Room.query.get(roomid)
            room.users.append(user)
            room.save()

            data = {
                "status": HTTP_OK,
                "msg": "加入房间成功",
                "data":room,
            }
            return marshal(data,single_room_fields)

        elif action==ROOM_ACTION_REGISTER:

            name =request.args.get("name")
            detail = request.args.get("detail")

            num = random.randint(10000, 100000)
            room=room.query.filter(Room.id==num).first()

            while room :
                num = random.randint(10000, 100000)
                room = room.query.filter(Room.id == num).first()
            num=str(user.id)+str(num)
            room = Room()

            room.url=num
            room.id=int(num)

            room.users.append(user)
            room.host_id=user.id
            room.name =name or "匿名聊天室"
            room.detail = detail

            room.save()
            data = {
                "status": HTTP_CREATE_OK,
                "msg": "房间创建成功",
                "data": room,
            }
            return  marshal(data,single_room_fields)


    @login_required
    def patch(self):
        args = parse_room_patch.parse_args()
        room=Room.query.get(args.get("roomid"))

        if not room:
            abort(404,msg="房间号不存在")

        user = g.user
        if user.id !=room.host_id:
            abort(403, msg="用户权限不足")


        name = args.get("name")
        detail = args.get("detail")
        icon = request.files.get("icon")


        if icon:
            icon.filename = secure_filename(icon.filename)
            icon.filename = change_filename(icon.filename)
            icon.filename = str(room.id) + icon.filename
            filepath = ROOM_DIR + icon.filename
            icon.save(filepath)

        room.name = name or room.name
        room.detail=detail or room.detail
        if icon:
            room.icon = icon.filename or room.icon
        room.save()

        data = {
            "msg": "房间信息修改成功",
            "status": HTTP_OK,
            "data": room
        }

        return marshal(data, single_room_fields)