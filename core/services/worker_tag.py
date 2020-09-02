# -*- coding: utf-8 -*-
import json
import traceback
from core.app import db
from flask import jsonify, request
from core.models.tag import TagModel
from core.schemas.tag import tag_schema, tags_schema


class WorkerTagService:
    """ Serviço responsável pela regra de negócio 
        e as requisições ao db """
    
    def create(self):
        name = request.json['name']
        
        tag_exist = TagModel.query.filter_by(name=name, isActive=True).first()
        result = tag_schema.dump(tag_exist)
        if tag_exist:
            return jsonify({
                'output': {
                    'data': result,
                    'message': 'tag already registered',
                    'error': None,
                    'isValid': False
                }
            }), 400
        
        tag = TagModel(name)
        try:
            db.session.add(tag)
            db.session.commit()
            result = tag_schema.dump(tag)
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
            tag = TagModel.query.filter_by(isActive=True).paginate(page, page_size)
            if tag:
                result = tags_schema.dump(tag.items)
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
            tag = TagModel.query.filter_by(uuid=id, isActive=True).first()
            if tag:
                result = tag_schema.dump(tag)
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
                    'message': "tag don't exist",
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
        
        tag = TagModel.query.filter_by(uuid=id, isActive=True).first()
        if not tag:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "tag don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            tag.name = name
            db.session.commit()
            result = tag_schema.dump(tag)
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
        tag = TagModel.query.filter_by(uuid=id, isActive=True).first()
        if not tag:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "tag don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            tag.isActive = False
            db.session.commit()
            result = tag_schema.dump(tag)
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
