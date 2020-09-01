# -*- coding: utf-8 -*-
from core.app import db
from core.app import marsh
from datetime import datetime
from core.utils.generate_uuid import generate_uuid


tagship = db.Table('tagship',
    db.Column('tag_uuid', db.String(), db.ForeignKey('tag.uuid'), primary_key=True),
    db.Column('task_uuid', db.String(), db.ForeignKey('task.uuid'), primary_key=True)
)

class TagshipSchema(marsh.Schema):
    """ Definição de schema de tagship """
    
    class Meta:
        model = tagship
        fields = (
            'tag_uuid',
            'task_uuid'
        )


class TaskModel(db.Model):
    """ Definição de modelo de task """
    
    __tablename__ = 'task'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(200), unique=True, nullable=False)
    notes = db.Column(db.String(), nullable=False)
    priority = db.Column(db.Enum('high', 'medium', 'low', name='priority'), nullable=False)
    remindMeOn = db.Column(db.DateTime)
    activityType = db.Column(db.Enum('indoors', 'outdoors', name='activityType'), nullable=False)
    status = db.Column(db.Enum('open', 'done', name='status'), nullable=False)
    taskList = db.Column(db.String(), db.ForeignKey('tasklist.uuid'), nullable=False)    
    tags = db.relationship("TagModel", secondary=tagship, lazy='subquery', backref=db.backref('tags', lazy=True))    
    create_on = db.Column(db.DateTime, default=datetime.utcnow)
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, title, notes, priority, remindMeOn, activityType, status, taskList, tags=None):
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
        model = TaskModel
        include_fk = True
        fields = (
            'uuid',
            'title',
            'notes',
            'priority',
            'remindMeOn',
            'activityType',
            'status',
            'taskList',
            'create_on',
            'tags'
        )

    tags = marsh.Nested(TagshipSchema, many=True)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
