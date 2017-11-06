# -*- coding: utf-8 -*-
from openerp import api, fields, models
import requests
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
import json

class ProductTempalteMembershipSignup(models.Model):

    _inherit = "product.template"
    
    signup_group_ids = fields.Many2many('res.groups', string="Sign up Groups", help="Groups the new users gets assigned to")
    extra_fields = fields.Many2many('ir.model.fields', string="Extra Fields", domain="[('model_id.model','=','res.partner'), ('ttype','=','char')]", help="Ask for extra informnation during signup")