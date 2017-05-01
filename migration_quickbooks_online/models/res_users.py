# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
from openerp import api, fields, models

class ResUsersQuickbooks(models.Model):

    _inherit = "res.users"

    quickbooks_oauth_access_token = fields.Char(string="Oauth Token")
    quickbooks_oauth_access_token_secret = fields.Char(string="Oauth Token Secret")
    quickbooks_realm_id = fields.Char(string="RealmID")