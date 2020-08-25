# -*- coding: utf-8 -*-
from flask.views import MethodView
from core.services.worker_tag import WorkerTagService
from flask import Blueprint


bp_tag = Blueprint('tag', __name__, url_prefix='/api')
class Tag(MethodView):
    

    def get(self, id=None):
        service = WorkerTagService()
        if id is None:
            return service.list()   
        else:
            return service.read(id=id)
                     

    def post(self):
        service = WorkerTagService()
        return service.create()
    
    
    def put(self, id):
        service = WorkerTagService()
        return service.update(id=id)


    def delete(self, id):
        service = WorkerTagService()
        return service.delete(id=id)


view = Tag.as_view('tag')
bp_tag.add_url_rule('/tags', view_func=view, methods=['GET'])
bp_tag.add_url_rule('/tags', view_func=view, methods=['POST'])
bp_tag.add_url_rule('/tags/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
