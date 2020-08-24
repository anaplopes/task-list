# -*- coding: utf-8 -*-
from core.app import db
from core.app import marsh
from datetime import datetime
from core.utils.generate_uuid import generate_uuid


class TaskListModel(db.Model):
    """ Definição de modelo de task list """
    
    __tablename__ = 'tasklist'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid())
    name = db.Column(db.String(100), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.now())
    isActive = db.Column(db.Boolean, default=True)
    task = db.relationship('TaskModel', backref='tasklist', lazy=True)
    
    def __init__(self, name):
        self.name = name


db.create_all()
db.session.commit()


class TaskListSchema(marsh.Schema):
    """ Definição de schema de task list """
    
    class Meta:
        fields = (
            'uuid',
            'name',
            'create_on'
        )


tasklist_schema = TaskListSchema()
tasklists_schema = TaskListSchema(many=True)