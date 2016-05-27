# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteOurModuleProjectTask(models.Model):

    _inherit = "project.task"
        
    custom_field_1 = fields.Char(string="Custom Field 1")
    custom_field_2 = fields.Char(string="Custom Field 2")
    custom_field_3 = fields.Char(string="Custom Field 3")
    custom_field_4 = fields.Char(string="Custom Field 4")
    custom_field_5 = fields.Char(string="Custom Field 5")