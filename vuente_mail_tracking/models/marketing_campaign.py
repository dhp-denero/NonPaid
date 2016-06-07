# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class MarketingCampaignTrackng(models.Model):

    _inherit = "marketing.campaign"
    
    email_tracking_sent = fields.Integer(string="Emails Sent", compute='_compute_email_tracking_sent')
    email_tracking_opened = fields.Integer(string="Emails Opened", compute='_compute_email_tracking_opened')

    def _compute_email_tracking_sent(self):
        self.email_tracking_sent = self.env['mail.mail.statistics'].search_count([('marketing_campaign_id','=',self.id), ('sent','!=', False)])
        
    def _compute_email_tracking_opened(self):
        self.email_tracking_opened = self.env['mail.mail.statistics'].search_count([('marketing_campaign_id','=',self.id), ('opened','!=', False)])