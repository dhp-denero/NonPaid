# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteResPartner(models.Model):

    _inherit = "res.partner"
        
    #has_image = fields.Boolean(string="Has Image")
    last_name = fields.Char(string="Last Name", size=64)
    birth_date = fields.Date(string="Birth Date", help="Send a birthday wish!")
    custom_field_1 = fields.Char()
    custom_field_2 = fields.Char()
    custom_field_3 = fields.Char()
    custom_field_4 = fields.Char()
    custom_field_5 = fields.Char()
    custom_field_6 = fields.Char()
    custom_field_7 = fields.Char()
    custom_field_8 = fields.Char()
    custom_field_9 = fields.Char()
    custom_field_10 = fields.Char()