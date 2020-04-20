import uuid

from flask import request, g
from flask_restful import Resource, reqparse, abort, fields, marshal
from werkzeug.utils import secure_filename

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_REGISTER, USER_ACTION_LOGIN, HTTP_OK, \
    USER_ACTION_QUICK_LOGIN, USER_VALIDATE
from App.apis.model_utils import get_user, login_required, change_filename
from App.models import User,Room
from App.settings import FC_DIR

parse_base = reqparse.RequestParser()
parse_base.add_argument("action", type=str, required=True, help="请输入请求参数")

parse_register = parse_base.copy()
parse_register.add_argument("password", type=str, required=True, help="请输入密码")
parse_register.add_argument("email", type=str, required=True, help="请输入邮箱")
parse_register.add_argument("username", type=str, required=True, help="请输入用户名")

parse_login = parse_base.copy()
parse_login.add_argument("password", type=str, required=True, help="请输入密码")
parse_login.add_argument("email", type=str, help="请输入邮箱")
parse_login.add_argument("username", type=str, help="请输入用户名")

parse_quick_login = parse_base.copy()
parse_quick_login.add_argument("username", type=str, required=True, help="请输入用户名")

parse_validate = parse_base.copy()
parse_validate.add_argument("token", type=str, required=True, help="请输入令牌")

parse_patch = reqparse.RequestParser()
parse_patch.add_argument("username", type=str)
parse_patch.add_argument("mood", type=str)
# parse_patch.add_argument("icon", type=str,location=['files'])


user_fields = {
    "username": fields.String,
    "mood": fields.String,
    "icon": fields.String,
    # "is_active":fields.Integer,
    "id":fields.Integer,
    "token":fields.String(attribute="access_token"),
}
single_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(user_fields),
}


class UserResource(Resource):
    def get(self):
        return {"msg": "ok"}

    def post(self):

        args = parse_base.parse_args()
        password = args.get("password")
        action = args.get("action").lower()

        if action == USER_ACTION_REGISTER:
            args_register = parse_register.parse_args()

            email = args_register.get("email")
            username = args_register.get("username")

            user = User()
            user.username = username
            user.set_password(password)
            user.email = email

            if not user.save():
                abort(400, msg="创建失败")

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "用户创建成功",
                "data": user,
            }
            return marshal(data, single_user_fields)

        elif action == USER_ACTION_LOGIN:
            args_login = parse_login.parse_args()

            email = args_login.get("email")
            username = args_login.get("username")

            user = get_user(username) or get_user(email)

            if not user:
                abort(400, msg="用户不存在")

            if not user.verify_password(password):
                abort(401, msg="用户名或密码错误")

            if user.is_delete:
                abort(401, msg="用户不存在")

            token = uuid.uuid4().hex
            user.access_token = token

            data = {
                "msg": "login success",
                "status": HTTP_OK,
                "token": token,
            }

            return data


        elif action == USER_ACTION_QUICK_LOGIN:
            args_quick_login = parse_quick_login.parse_args()
            username = args_quick_login.get("username")

            user = get_user(username)
            if user:
                abort(400, msg="用户名已经存在")

            user = User()
            user.username = username
            # user.ip=ip

            if not user.save():
                abort(400, msg="创建失败")
            room = Room.query.get(1)
            room.users.append(user)
            room.save()
            token = uuid.uuid4().hex
            user.access_token = token
            user.save()
            data = {
                "msg": "quick_login success",
                "status": HTTP_OK,
                "token": token,
                "data": user,
            }
            return marshal(data, single_user_fields)

        elif action == USER_VALIDATE:
            args = parse_validate.parse_args()
            token = args.get("token")
            if token:
                user = get_user(token)
                if user:
                    data = {
                        "msg": "validate pass",
                        "status": HTTP_OK,
                        "token": token,
                        "data": user,
                    }
                    return marshal(data, single_user_fields)
            abort(400, msg="validate failed")
        else:
            abort(400, msg="请提供正确的参数")

    @login_required
    def patch(self):
        args = parse_patch.parse_args()

        user = g.user

        username = args.get("username")
        name_count = User.query.filter_by(username=username).count()
        if username != user.username and name_count == 1:
            abort(400, msg="用户名已经存在")

        mood = args.get("mood")
        # icon=args.get("icon")
        icon = request.files.get("icon")
        # print(icon)

        if icon:
            icon.filename = secure_filename(icon.filename)
            icon.filename = change_filename(icon.filename)
            icon.filename = str(user.id) + icon.filename
            filepath = FC_DIR + icon.filename
            icon.save(filepath)

        user.username = username or user.username
        user.mood = mood or user.mood
        if icon:
            user.icon = icon.filename or user.icon
        user.save()

        data = {
            "msg": "用户信息修改成功",
            "status": HTTP_OK,
            "data": user
        }

        return marshal(data, single_user_fields)
