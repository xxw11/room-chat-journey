import uuid

from flask import request
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_CREATE_OK, USER_ACTION_REGISTER, USER_ACTION_LOGIN, HTTP_OK, \
    USER_ACTION_QUICK_LOGIN, USER_VALIDATE
from App.apis.model_utils import get_user
from App.ext import cache
from App.models import User

parse_base=reqparse.RequestParser()
parse_base.add_argument("action", type=str, required=True, help="请输入请求参数")


parse_register =parse_base.copy()
parse_register.add_argument("password", type=str, required=True, help="请输入密码")
parse_register.add_argument("email", type=str, required=True, help="请输入邮箱")
parse_register.add_argument("username", type=str, required=True, help="请输入用户名")

parse_login =parse_base.copy()
parse_login.add_argument("password", type=str, required=True, help="请输入密码")
parse_login.add_argument("email", type=str, help="请输入邮箱")
parse_login.add_argument("username", type=str, help="请输入用户名")

parse_quick_login =parse_base.copy()
parse_quick_login.add_argument("username", type=str,required=True, help="请输入用户名")

parse_validate =parse_base.copy()
parse_validate.add_argument("token", type=str,required=True, help="请输入令牌")


user_fields={
    "username": fields.String,
    "email":fields.String,
    "permission":fields.Integer,
    "is_active":fields.Integer,
}
single_user_fields={
    "status":fields.Integer,
    "msg":fields.String,
    "data":fields.Nested(user_fields),
}
class UserResource(Resource):
    def get(self):
        return {"msg":"ok"}

    def post(self):

        args = parse_base.parse_args()
        password = args.get("password")
        action =args.get("action").lower()

        if action ==USER_ACTION_REGISTER:
            args_register=parse_register.parse_args()

            email = args_register.get("email")
            username = args_register.get("username")

            user=User()
            user.username=username
            user.set_password(password)
            user.email=email

            if not user.save():
                abort(400,msg="创建失败")

            data={
                "status":HTTP_CREATE_OK,
                "msg":"用户创建成功",
                "data": user,
            }
            return marshal(data,single_user_fields)

        elif action==USER_ACTION_LOGIN:
            args_login = parse_login.parse_args()

            email = args_login.get("email")
            username = args_login.get("username")

            user=get_user(username)or get_user(email)

            if not user:
                abort(400,msg="用户不存在")

            if not user.verify_password(password):
                abort(401,msg="用户名或密码错误")

            if user.is_delete:
                abort(401,msg="用户不存在")

            token=uuid.uuid4().hex
            user.access_token=token


            data={
                "msg":"login success",
                "status":HTTP_OK,
                "token":token,
            }

            return data


        elif action == USER_ACTION_QUICK_LOGIN:
            args_quick_login = parse_quick_login.parse_args()
            username = args_quick_login.get("username")

            user = get_user(username)
            if user:
                abort(400, msg="用户名已经存在")

            user=User()
            user.username=username
            # user.ip=ip

            if not user.save():
                abort(400,msg="创建失败")

            token = uuid.uuid4().hex
            user.access_token=token
            user.save()
            data = {
                "msg": "quick_login success",
                "status": HTTP_OK,
                "token": token,
                "username":username,
            }
            return data

        elif action==USER_VALIDATE:
            args= parse_validate.parse_args()
            token=args.get("token")
            if token :
                user = get_user(token)
                if user :
                    data = {
                        "msg": "validate pass",
                        "status": HTTP_OK,
                        "token": token,
                        "username": user.username,
                    }
                    return data
            abort(400, msg="validate failed")
        else:
            abort(400,msg="请提供正确的参数")

    def patch(self):
        return {"msg":"ok"}
