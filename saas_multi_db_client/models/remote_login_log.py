# -*- coding: utf-8 -*-
from openerp import api, fields, models

class RemoteLoginLog(models.Model):

    _name = "remote.login.log"
    
    user_name = fields.Char(string="User Name")
    ref_url = fields.Char(string="Ref URL")