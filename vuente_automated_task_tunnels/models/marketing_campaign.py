# -*- coding: utf-8 -*-
from datetime import datetime

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MarketingCampaignFilter(models.Model):

    _inherit = "marketing.campaign"
    
    sort_type = fields.Selection([('task','Task'), ('email','Email'), ('sms','SMS')], string="Type")
    vuente_from_email = fields.Char(string="From Email")
    vuente_mail_server = fields.Many2one('ir.mail_server', string="Mail Server")
    vuente_reply_to = fields.Char(string="Reply To")