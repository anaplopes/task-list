# -*- coding: utf-8 -*-
from core.app import db
from datetime import datetime
from core.utils.generate_uuid import generate_uuid


class TagModel(db.Model):
    """ Definição de modelo de tag """
    
    __tablename__ = 'tag'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)
    create_on = db.Column(db.DateTime, default=datetime.utcnow)
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, name, count=None):
        self.name = name
        self.count = count
