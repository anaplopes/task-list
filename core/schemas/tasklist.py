# -*- coding: utf-8 -*-
from core.app import marsh
from core.models.tasklist import TaskListModel


class TaskListSchema(marsh.Schema):
    """ Definição de schema de task list """
    
    class Meta:
        model = TaskListModel
        fields = (
            'uuid',
            'name',
            'create_on'
        )


tasklist_schema = TaskListSchema()
tasklists_schema = TaskListSchema(many=True)
