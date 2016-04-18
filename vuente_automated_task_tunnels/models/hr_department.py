# -*- coding: utf-8 -*-
from openerp import api, fields, models

class HrDepartment(models.Model):

    _inherit = "hr.department"
    
    task_ids = fields.One2many('project.task', 'department_id', string="Tasks")
    employee_ids = fields.Many2many('hr.employee', string="Employees")