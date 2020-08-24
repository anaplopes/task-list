# -*- coding: utf-8 -*-
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONNECTION_URL_DEFAULT = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.getenv('CONNECTION_URL', CONNECTION_URL_DEFAULT)
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
