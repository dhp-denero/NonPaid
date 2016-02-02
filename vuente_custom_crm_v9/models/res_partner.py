# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteResPartner(models.Model):

    _inherit = "res.partner"
        
    last_name = fields.Char(string="Last Name", size=64)
    birth_date = fields.Date(string="Birth Date", help="Send a birthday wish!")