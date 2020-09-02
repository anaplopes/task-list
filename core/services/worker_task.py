# -*- coding: utf-8 -*-
import json
import traceback
from core.app import db
from datetime import datetime
from flask import jsonify, request
from core.models.tag import TagModel
from core.models.task import TaskModel
from core.schemas.tag import tag_schema, tags_schema
from core.schemas.task import task_schema, tasks_schema


class WorkerTaskService:
    """ Serviço responsável pela regra de negócio 
        e as requisições ao db """
    
    def create(self):
        title = request.json['title']
        notes = request.json['notes']
        priority = request.json['priority']
        activityType = request.json['activityType']
        status = request.json['status']
        taskList = request.json['taskList']
        tags = request.json['tags']
        
        remindMeOn = request.json['remindMeOn']
        if remindMeOn:
            remindMeOn = datetime.strptime(request.json['remindMeOn'], '%Y-%m-%dT%H:%M:%S.%f')
        
        task_exist = TaskModel.query.filter_by(title=title, isActive=True).first()
        result = task_schema.dump(task_exist)
        if task_exist:
            return jsonify({
                'output': {
                    'data': result,
                    'message': 'task already registered',
                    'error': None,
                    'isValid': False
                }
            }), 400
        
        try:
            tag_list = []
            for each in tags:
                tag = TagModel.query.filter_by(name=each, isActive=True).first()
                if not tag:
                    tag = TagModel(name=each, count=1)
                else:
                    tag.count += 1
                
                tag_list.append(tag)
                
            task = TaskModel(title, notes, priority, remindMeOn, activityType, status, taskList, tag_list)
            db.session.add(task)
            db.session.commit()
            result = task_schema.dump(task)
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
            task = TaskModel.query.filter_by(isActive=True).paginate(page, page_size)
            if task:
                result = tasks_schema.dump(task.items)
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
            task = TaskModel.query.filter_by(uuid=id, isActive=True).first()
            if task:
                result = task_schema.dump(task)
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
                    'message': "task don't exist",
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
        title = request.json['title']
        notes = request.json['notes']
        priority = request.json['priority']
        remindMeOn = request.json['remindMeOn']
        activityType = request.json['activityType']
        status = request.json['status']
        taskList = request.json['taskList']
        tags = request.json['tags']
        
        task = TaskModel.query.filter_by(uuid=id, isActive=True).first()
        if not task:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "task don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            task.title = title
            task.notes = notes
            task.priority = priority
            task.remindMeOn = remindMeOn
            task.activityType = activityType
            task.status = status
            task.taskList = taskList
            task.tags = tags
            db.session.commit()
            result = task_schema.dump(task)
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
        task = TaskModel.query.filter_by(uuid=id, isActive=True).first()
        if not task:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "task don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            task.isActive = False
            db.session.commit()
            result = task_schema.dump(task)
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
