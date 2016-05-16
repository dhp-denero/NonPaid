# -*- coding: utf-8 -*-
from openerp import api, fields, models

class MailTemplateTunnel(models.Model):

    _inherit = "mail.template"
    
    advanced_settings = fields.Boolean(string="Advanced Settings")