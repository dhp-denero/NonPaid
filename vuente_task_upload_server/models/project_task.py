# -*- coding: utf-8 -*-
from openerp import api, fields, models

import werkzeug

class ProjectTaskUploadServer(models.Model):

    _inherit = "project.task"
    
    remote_task_id = fields.Integer(string="Remote Task ID")
    remote_task_host = fields.Char(string="Host")
    remote_task_url = fields.Char(string="Remote Task URL")