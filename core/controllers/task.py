# -*- coding: utf-8 -*-
from flask.views import MethodView
from core.services.worker_task import WorkerTaskService
from flask import Blueprint


bp_task = Blueprint('task', __name__, url_prefix='/api')
class Task(MethodView):
    

    def get(self, id=None):
        service = WorkerTaskService()
        if id is None:
            return service.worker.list()   
        else:
            return service.worker.read(id=id)
                     

    def post(self):
        service = WorkerTaskService()
        return service.worker.create()
    
    
    def put(self, id):
        service = WorkerTaskService()
        return service.worker.update(id=id)


    def delete(self, id):
        service = WorkerTaskService()
        return service.worker.delete(id=id)


view = Task.as_view('task')
bp_task.add_url_rule('/tasks', view_func=view, methods=['GET'])
bp_task.add_url_rule('/tasks', view_func=view, methods=['POST'])
bp_task.add_url_rule('/tasks/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
