# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteFinanceResPartner(models.Model):

    _inherit = "res.partner"
        
    finance_custom_field_1 = fields.Char(string="Custom Field 1")
    finance_custom_field_2 = fields.Char(string="Custom Field 2")
    finance_custom_field_3 = fields.Char(string="Custom Field 3")
    finance_custom_field_4 = fields.Char(string="Custom Field 4")
    finance_custom_field_5 = fields.Char(string="Custom Field 5")
    finance_custom_field_6 = fields.Char(string="Custom Field 6")
    finance_custom_field_7 = fields.Char(string="Custom Field 7")
    finance_custom_field_8 = fields.Char(string="Custom Field 8")
    finance_custom_field_9 = fields.Char(string="Custom Field 9")
    finance_custom_field_10 = fields.Char(string="Custom Field 10")