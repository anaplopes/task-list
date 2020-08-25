# -*- coding: utf-8 -*-
from flask.views import MethodView
from core.services.worker_task import WorkerTaskService
from flask import Blueprint


bp_task = Blueprint('task', __name__, url_prefix='/api')
class Task(MethodView):
    

    def get(self, id=None):
        service = WorkerTaskService()
        if id is None:
            return service.list()   
        else:
            return service.read(id=id)
                     

    def post(self):
        return WorkerTaskService().create()
    
    
    def put(self, id):
        return WorkerTaskService().update(id=id)


    def delete(self, id):
        return WorkerTaskService().delete(id=id)


view = Task.as_view('task')
bp_task.add_url_rule('/tasks', view_func=view, methods=['GET'])
bp_task.add_url_rule('/tasks', view_func=view, methods=['POST'])
bp_task.add_url_rule('/tasks/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
