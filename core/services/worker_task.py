# -*- coding: utf-8 -*-
import json
import traceback
from core.app import db
from flask import jsonify, request
# from core.models.user import UserModel, user_schema, users_schema


class WorkerTaskService:
    """ Serviço responsável pela regra de negócio 
        e as requisições ao db """
    
    # def create(self):
    #     username = request.json['username']
    #     password = request.json['password']
    #     name = request.json['name']
    #     email = request.json['email']
    #     address = request.json['address']
    #     city = request.json['city']
    #     country = request.json['country']
        
    #     user_exist = UserModel.query.filter_by(username=username, isActive=True).first()
    #     result = user_schema.dump(user_exist)
    #     if user_exist:
    #         return jsonify({
    #             'output': {
    #                 'data': result,
    #                 'message': 'user already registered',
    #                 'error': None,
    #                 'isValid': False
    #             }
    #         }), 400
        
    #     user = UserModel(username, pass_hash, name, email, address, city, country)
    #     try:
    #         db.session.add(user)
    #         db.session.commit()
    #         result = user_schema.dump(user)
    #         return jsonify({
    #             'output': {
    #                 'data': result,
    #                 'message': 'successfully registered',
    #                 'error': None,
    #                 'isValid': True
    #             }
    #         }), 201

    #     except Exception:
    #         db.session.rollback()
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': 'unable to create',
    #                 'error': traceback.format_exc(),
    #                 'isValid': False
    #             }
    #         }), 500

    
    # def list(self):
    #     page = int(request.args.get('page')) if request.args.get('page') else 1
    #     page_size = int(request.args.get('pageSize')) if request.args.get('pageSize') else 10
        
    #     try:
    #         user = UserModel.query.filter_by(isActive=True).paginate(page, page_size)
    #         if user:
    #             result = users_schema.dump(user.items)
    #             return jsonify({
    #                 'output': {
    #                     'data': result,
    #                     'qtd_registro': len(result),
    #                     'message': 'successfully fetched',
    #                     'error': None,
    #                     'isValid': True
    #                 }
    #             }), 200
            
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': 'nothing found',
    #                 'error': None,
    #                 'isValid': False
    #             }
    #         }), 404

    #     except Exception:
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': None,
    #                 'error': traceback.format_exc(),
    #                 'isValid': False
    #             }
    #         }), 500
    
    
    # def read(self, id):
    #     try:
    #         user = UserModel.query.filter_by(uuid=id, isActive=True).first()
    #         if user:
    #             result = user_schema.dump(user)
    #             return jsonify({
    #                 'output': {
    #                     'data': result,
    #                     'message': 'successfully fetched',
    #                     'error': None,
    #                     'isValid': True
    #                 }
    #             }), 200
            
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': "user don't exist",
    #                 'error': None,
    #                 'isValid': False
    #             }
    #         }), 404

    #     except Exception:
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': None,
    #                 'error': traceback.format_exc(),
    #                 'isValid': False
    #             }
    #         }), 500
    
            
    # def update(self, id):
    #     username = request.json['username']
    #     password = request.json['password']
    #     name = request.json['name']
    #     email = request.json['email']
    #     address = request.json['address']
    #     city = request.json['city']
    #     country = request.json['country']
        
    #     user = UserModel.query.filter_by(uuid=id, isActive=True).first()
    #     if not user:
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': "user don't exist",
    #                 'error': None,
    #                 'isValid': False
    #             }
    #         }), 404
        
    #     pass_hash = generate_password_hash(password)
    #     try:
    #         user.username = username
    #         user.password = pass_hash
    #         user.name = name
    #         user.email = email
    #         user.address = address
    #         user.city = city
    #         user.country = country
    #         db.session.commit()
    #         result = user_schema.dump(user)
    #         return jsonify({
    #             'output': {
    #                 'data': result,
    #                 'message': 'successfully updated',
    #                 'error': None,
    #                 'isValid': True
    #             }
    #         }), 201

    #     except Exception:
    #         db.session.rollback()
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': 'unable to update',
    #                 'error': traceback.format_exc(),
    #                 'isValid': False
    #             }
    #         }), 500
    
    
    # def delete(self, id):
    #     user = UserModel.query.filter_by(uuid=id, isActive=True).first()
    #     if not user:
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': "user don't exist",
    #                 'error': None,
    #                 'isValid': False
    #             }
    #         }), 404
        
    #     try:
    #         user.isActive = False
    #         db.session.commit()
    #         result = user_schema.dump(user)
    #         return jsonify({
    #             'output': {
    #                 'data': result,
    #                 'message': 'successfully deleted',
    #                 'error': None,
    #                 'isValid': True
    #             }
    #         }), 200

    #     except Exception:
    #         db.session.rollback()
    #         return jsonify({
    #             'output': {
    #                 'data': [],
    #                 'message': 'unable to delete',
    #                 'error': traceback.format_exc(),
    #                 'isValid': False
    #             }
    #         }), 500
