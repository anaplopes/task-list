# -*- coding: utf-8 -*-
from core.app import ma
from core.models.tag import TagModel


class TagSchema(ma.Schema):
    """ Definição de schema de tags """
    
    class Meta:
        model = TagModel
        fields = (
            'uuid',
            'name',
            'count',
            'create_on'
        )


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
