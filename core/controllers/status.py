# -*- coding: utf-8 -*-
import json
import setup
from datetime import datetime
from core.app import started_date
from flask.views import MethodView
from flask import Blueprint, jsonify


bp_status = Blueprint('status', __name__, url_prefix='/')
class Live(MethodView):

    def get(self):
        payload = {
            'name': setup.name,
            'version': setup.version,
            'started': started_date,
            'uptime': str(datetime.now() - started_date)
        }
        return jsonify(payload), 200


view = Live.as_view('status')
bp_status.add_url_rule('/', view_func=view, methods=['GET'])
