from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db

class BaseModel(db.Model):
    __abstract__=True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as  e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as  e:
            print(e)
            return False



class User(BaseModel):
    access_token = db.Column(db.String(128))
    email = db.Column(db.String(254))
    username = db.Column(db.String(30),unique=True)
    # password = db.Column(db.String(128))
    permission = db.Column(db.Integer,default=1)
    is_active =db.Column(db.Integer,default=0)
    is_delete =db.Column(db.Integer,default=0)
    # ip = db.Column(db.String(255))
    # bio = db.Column(db.String(120))

    messages = db.relationship('Message', backref='user', cascade='all')
    # own_rooms = db.relationship('Room', backref='host', cascade='all')
    u_rooms=db.Column(db.Integer, db.ForeignKey('room.id'), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Room(BaseModel):

    name=db.Column(db.String(64),default='匿名聊天室')
    url= db.Column(db.String(255))

    host_id = db.Column(db.Integer, nullable=True)
    users = db.relationship('User', secondary='u_r',backref='rooms')

    messages = db.relationship('Message', backref='m_room', cascade='all')

    __tablename__ = 'room'


class Message(BaseModel):
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(), index=True)


    message_author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message_room = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)


u_r = db.Table('u_r',
               db.Column('u_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
               db.Column('r_id', db.Integer, db.ForeignKey('room.id'), primary_key=True),
               )