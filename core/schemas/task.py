# -*- coding: utf-8 -*-
from core.app import ma
from core.models.task import TaskModel
from core.schemas.tag import TagSchema


class TaskSchema(ma.Schema):
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
            'tags',
            'create_on'
        )

    tags = ma.Nested(TagSchema, many=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
