# -*- coding: utf-8 -*-
from datetime import datetime

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MarketingCampaignTestMember(models.Model):

    _name = "marketing.campaign.test.member"
    
    campaign_id = fields.Many2one('marketing.campaign', string="Campaign")
    partner_id = fields.Many2one('res.partner', string="Partner")
    
    @api.multi
    def run_test(self):
        """Goes through all activities in the campaign, creates workitems for them and processes them"""

        self.ensure_one()
                
        #Add the new partner to a campaign
        for act in self.campaign_id.activity_ids:
            wi = self.env['marketing.campaign.workitem'].sudo().create({'campaign_id': self.campaign_id.id, 'activity_id': act.id, 'partner_id': self.partner_id.id, 'res_id': self.partner_id.id, 'testid': self.id})
            wi.vuente_test_process()
            
        #Force emails out
        self.env['mail.mail'].process_email_queue()
        
        return {'type': 'ir.actions.act_window',
	        'res_model': 'marketing.campaign.workitem',
	        'view_type': 'form',
	        'view_mode': 'tree,form',
	        'context': "{'search_default_testid': " + str(self.id) + "}",
	        'target': 'current'}
