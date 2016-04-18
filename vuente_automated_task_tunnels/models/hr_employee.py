# -*- coding: utf-8 -*-
from openerp import api, fields, models

class HrEmployee(models.Model):

    _inherit = "hr.employee"
    
    department_ids = fields.Many2many('hr.department', string="Departments")
