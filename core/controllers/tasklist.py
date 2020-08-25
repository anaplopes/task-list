# -*- coding: utf-8 -*-
from flask.views import MethodView
from core.services.worker_tasklist import WorkerTaskListService
from flask import Blueprint


bp_tasklist = Blueprint('tasklist', __name__, url_prefix='/api')
class TaskList(MethodView):
    

    def get(self, id=None):
        service = WorkerTaskListService()
        if id is None:
            return service.list()   
        else:
            return service.read(id=id)
                     

    def post(self):
        service = WorkerTaskListService()
        return service.create()
    
    
    def put(self, id):
        service = WorkerTaskListService()
        return service.update(id=id)


    def delete(self, id):
        service = WorkerTaskListService()
        return service.delete(id=id)


view = TaskList.as_view('tasklist')
bp_tasklist.add_url_rule('/taskList', view_func=view, methods=['GET'])
bp_tasklist.add_url_rule('/taskList', view_func=view, methods=['POST'])
bp_tasklist.add_url_rule('/taskList/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
