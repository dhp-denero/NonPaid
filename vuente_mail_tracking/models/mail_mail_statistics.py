# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class MailMailStatisticsCampaign(models.Model):

    _inherit = "mail.mail.statistics"
    
    marketing_campaign_id = fields.Many2one('marketing.campaign', string="Marketing Campaign")
    mail_template_id = fields.Many2one('mail.template', string="Mail Template")