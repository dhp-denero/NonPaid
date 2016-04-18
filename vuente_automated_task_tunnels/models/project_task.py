# -*- coding: utf-8 -*-
from openerp import api, fields, models

class ProjectTask(models.Model):

    _inherit = "project.task"
    
    department_id = fields.Many2one('hr.department', string="Department")
