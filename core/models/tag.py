# -*- coding: utf-8 -*-
from core.app import db
from core.app import marsh
from datetime import datetime
from core.utils.generate_uuid import generate_uuid


class TagModel(db.Model):
    """ Definição de modelo de tag """
    
    __tablename__ = 'tag'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid())
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)
    create_on = db.Column(db.DateTime(timezone=True), default=datetime.now())
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, name):
        self.name = name

db.create_all()
db.session.commit()

class TagSchema(marsh.Schema):
    """ Definição de schema de tags """
    
    class Meta:
        fields = (
            'uuid',
            'name',
            'count',
            'create_on'
        )


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
