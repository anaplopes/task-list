# -*- coding: utf-8 -*-
from flask.views import MethodView
from core.services.worker_tasklist import WorkerTaskListService
from flask import Blueprint


bp_tasklist = Blueprint('tasklist', __name__, url_prefix='/api')
class TaskList(MethodView):
    

    def __init__(self):
        self.worker = WorkerTaskListService()
    

    def get(self, id=None):
        if id is None:
            return self.worker.list()   
        else:
            return self.worker.read(id=id)
                     

    def post(self):
        return self.worker.create()
    
    
    def put(self, id):
        return self.worker.update(id=id)


    def delete(self, id):
        return self.worker.delete(id=id)


view = TaskList.as_view('tasklist')
bp_tasklist.add_url_rule('/taskList', view_func=view, methods=['GET'])
bp_tasklist.add_url_rule('/taskList', view_func=view, methods=['POST'])
bp_tasklist.add_url_rule('/taskList/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
