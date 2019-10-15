# -*- coding: utf-8 -*-

from osv import osv, field, orm

class obj_inscription(osv.osv):
    _name = "obj.inscription"
    _description = "Objet inscription"
    _columns = {
        'name': fields.char("Nom", required=True),
        'cin': fields.char("CIN", required=True),
        'datenais': fields.date("Date de naissance"),
        'image': fields.binary("Image"),
    }

    _default = {
        'name': "Name",
    }