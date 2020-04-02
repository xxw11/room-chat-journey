from flask import request, g
from flask_restful import abort

from App.ext import cache
from App.models import User

# 查询用户
def get_user(user_ident):
    if not user_ident:
        return None

    #根据id
    user = User.query.get(user_ident)

    if user:
        return user
    #根据token
    user=User.query.filter(User.access_token==user_ident).first()
    if user:
        return user

    user = User.query.filter(User.email==user_ident).first()

    if user:
        return user

    user = User.query.filter(User.username==user_ident).first()

    if user:
        return user
    return None

# 访问控制
def login_required(fun):
    def wrapper(*args,**kwargs):
        token=request.args.get("token")

        user=get_user(token)

        if not user:
            abort(401, msg="user not available")

        g.user= user
        g.auth= token

        return fun(*args,**kwargs)
    return wrapper