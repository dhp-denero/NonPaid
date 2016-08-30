# -*- coding: utf-8 -*-
from datetime import datetime

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MarketingCampaignTranition(models.Model):

    _inherit = "marketing.campaign.transition"
    
    campaign_id = fields.Many2one('marketing.campaign', string="Campaign")
    trigger = fields.Selection(selection_add=[('email_open', 'Email Opened')])