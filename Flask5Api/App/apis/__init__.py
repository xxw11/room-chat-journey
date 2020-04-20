from flask_restful import Api

from App import models


# from App.apis.affairs_api import AffairResource, AffairsResource, AffairSortResource, AffairAddResource
#
#
from App.apis.message_api import MessageResource, RoomMsgResource, MsgPictureResource
from App.apis.room_api import RoomResource
from App.apis.user_api import UserResource

api = Api()
#
#
def init_api(app):
    api.init_app(app)

api.add_resource(UserResource,'/api/user/')
api.add_resource(RoomResource,'/api/room/')
api.add_resource(RoomMsgResource,'/api/msg/')
api.add_resource(MsgPictureResource,'/api/msg/picture/')
api.add_resource(MessageResource,'/api/ws/')

