# -*- coding: utf-8 -*-
from datetime import datetime

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MarketingCampaignFilter(models.Model):

    _inherit = "marketing.campaign"
    
    transition_ids = fields.One2many('marketing.campaign.transition', 'campaign_id', string="Transitions")