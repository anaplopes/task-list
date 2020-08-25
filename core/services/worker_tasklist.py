# -*- coding: utf-8 -*-
import json
import traceback
from core.app import db
from flask import jsonify, request
from core.models.tasklist import TaskListModel, tasklist_schema, tasklists_schema


class WorkerTaskListService:
    """ Serviço responsável pela regra de negócio 
        e as requisições ao db """
    
    def create(self):
        name = request.json['name']
        
        tasklist_exist = TaskListModel.query.filter_by(name=name, isActive=True).first()
        result = tasklist_schema.dump(tasklist_exist)
        if tasklist_exist:
            return jsonify({
                'output': {
                    'data': result,
                    'message': 'task list already registered',
                    'error': None,
                    'isValid': False
                }
            }), 400
        
        tasklist = TaskListModel(name)
        try:
            db.session.add(tasklist)
            db.session.commit()
            result = tasklist_schema.dump(tasklist)
            return jsonify({
                'output': {
                    'data': result,
                    'message': 'successfully registered',
                    'error': None,
                    'isValid': True
                }
            }), 201

        except Exception:
            db.session.rollback()
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'unable to create',
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500

    
    def list(self):
        page = int(request.args.get('page')) if request.args.get('page') else 1
        page_size = int(request.args.get('pageSize')) if request.args.get('pageSize') else 10
        
        try:
            tasklist = TaskListModel.query.filter_by(isActive=True).paginate(page, page_size)
            if tasklist:
                result = tasklists_schema.dump(tasklist.items)
                return jsonify({
                    'output': {
                        'data': result,
                        'qtd_registro': len(result),
                        'message': 'successfully fetched',
                        'error': None,
                        'isValid': True
                    }
                }), 200
            
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'nothing found',
                    'error': None,
                    'isValid': False
                }
            }), 404

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': None,
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
    
    def read(self, id):
        try:
            tasklist = TaskListModel.query.filter_by(uuid=id, isActive=True).first()
            if tasklist:
                result = tasklist_schema.dump(tasklist)
                return jsonify({
                    'output': {
                        'data': result,
                        'message': 'successfully fetched',
                        'error': None,
                        'isValid': True
                    }
                }), 200
            
            return jsonify({
                'output': {
                    'data': [],
                    'message': "task list don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': None,
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
            
    def update(self, id):
        name = request.json['name']
        
        tasklist = TaskListModel.query.filter_by(uuid=id, isActive=True).first()
        if not tasklist:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "task list don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            tasklist.name = name
            db.session.commit()
            result = tasklist_schema.dump(tasklist)
            return jsonify({
                'output': {
                    'data': result,
                    'message': 'successfully updated',
                    'error': None,
                    'isValid': True
                }
            }), 201

        except Exception:
            db.session.rollback()
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'unable to update',
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
    
    def delete(self, id):
        tasklist = TaskListModel.query.filter_by(uuid=id, isActive=True).first()
        if not tasklist:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "task list don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            tasklist.isActive = False
            db.session.commit()
            result = tasklist_schema.dump(tasklist)
            return jsonify({
                'output': {
                    'data': result,
                    'message': 'successfully deleted',
                    'error': None,
                    'isValid': True
                }
            }), 200

        except Exception:
            db.session.rollback()
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'unable to delete',
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
