# -*- coding: utf-8 -*-
from openerp import api, fields, models

class TaskTemplate(models.Model):

    _name = "task.template"
    
    name = fields.Char(string="Name")
    department_id = fields.Many2one('hr.department', string="Department")
    description = fields.Text(string="Description")