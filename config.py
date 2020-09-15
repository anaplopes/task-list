# -*- coding: utf-8 -*-
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Base configuration """
    
    DEBUG = False
    TESTING = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DATABASE_URI_DEFAULT = 'sqlite:///' + os.path.join(basedir, 'app.db')


class ProductionConfig(BaseConfig):
    """ Production configuration """
    
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('CONNECTION_URL', '')


class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """ Testing configuration """
    
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False
