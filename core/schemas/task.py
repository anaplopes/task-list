# -*- coding: utf-8 -*-
from core.app import marsh
from core.models.tag import TagSchema
from core.models.task import TaskModel


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
            'tags',
            'create_on'
        )

    tags = marsh.Nested(TagSchema, many=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
