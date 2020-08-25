# -*- coding: utf-8 -*-
from core.app import db
from core.app import marsh
from datetime import datetime
from core.utils.generate_uuid import generate_uuid


tags = db.Table('tags',
    db.Column('uuid', db.String(), primary_key=True, default=generate_uuid()),
    db.Column('tag_uuid', db.String(), db.ForeignKey('tag.uuid')),
    db.Column('task_uuid', db.String(), db.ForeignKey('task.uuid'))
)

class TaskModel(db.Model):
    """ Definição de modelo de task """
    
    __tablename__ = 'task'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid())
    title = db.Column(db.String(200), unique=True, nullable=False)
    notes = db.Column(db.String(), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    remindMeOn = db.Column(db.DateTime(timezone=True))
    activityType = db.Column(db.String())
    status = db.Column(db.String(4), nullable=False)
    taskList = db.Column(db.String(), db.ForeignKey('tasklist.uuid'), nullable=False)
    tags = db.relationship('TagModel', secondary=tags, backref=db.backref('taglist', lazy='dynamic'))
    create_on = db.Column(db.DateTime(timezone=True), default=datetime.now())
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, title, notes, priority, remindMeOn, activityType, status, taskList, tags):
        self.title = title
        self.notes = notes
        self.priority = priority
        self.remindMeOn = remindMeOn
        self.activityType = activityType
        self.status = status
        self.taskList = taskList
        self.tags = tags



class TaskSchema(marsh.Schema):
    """ Definição de schema de tasks """
    
    class Meta:
        fields = (
            'uuid',
            'title',
            'notes',
            'priority',
            'remindMeOn',
            'activityType',
            'status',
            'taskList',
            'tags',
            'create_on'
        )


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
