# -*- coding: utf-8 -*-
from core.app import db
from core.app import marsh
from datetime import datetime
from core.utils.generate_uuid import generate_uuid
from core.utils.generate_avatar import generate_avatar


class UserModel(db.Model):
    """ Definição de modelo de usuário """
    
    __tablename__ = 'user'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid())
    avatar = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.now())
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, username, password, name, email, address, city, country, avatar=None):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.address = address
        self.city = city
        self.country = country
        self.avatar = generate_avatar(self.email)

db.create_all()
db.session.commit()


class UserSchema(marsh.Schema):
    """ Definição de schema de usuários """
    
    class Meta:
        fields = (
            'uuid',
            'avatar',
            'username',
            'password',
            'name',
            'email',
            'address',
            'city',
            'country',
            'create_on'
        )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
