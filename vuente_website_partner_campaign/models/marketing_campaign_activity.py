# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp.osv import osv

from openerp import api, fields, models

class MarketingCampaignActivityMailTracking(osv.osv):

    _inherit = "marketing.campaign.activity"
    
    def _process_wi_email(self, cr, uid, activity, workitem, context=None):
        my_campaign = self.pool.get('marketing.campaign.activity').browse(cr, uid, int(activity.id) ).campaign_id.id
        return self.pool.get('mail.template').send_mail_track(cr, uid,
                                            activity.email_template_id.id,
                                            workitem.res_id, my_campaign, context=context)