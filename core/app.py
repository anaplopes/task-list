# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app)
started_date = datetime.now()

# config database
app_settings = os.getenv(
    'APP_SETTINGS',
    'config.DevelopmentConfig'
)
app.config.from_object(app_settings)
db = SQLAlchemy(app)
marsh = Marshmallow(app)

# model
from core.models import user

# blueprint
from core.controllers.status import bp_status
app.register_blueprint(bp_status)

from core.controllers.tag import bp_tag
app.register_blueprint(bp_tag)

from core.controllers.task import bp_task
app.register_blueprint(bp_task)

from core.controllers.tasklist import bp_tasklist
app.register_blueprint(bp_tasklist)
