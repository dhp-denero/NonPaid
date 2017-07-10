# -*- coding: utf-8 -*-
from datetime import datetime
import uuid
import urlparse
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class MarketingCampaignReverse(models.Model):

    _inherit = "marketing.campaign"
    
    direction = fields.Selection([('forward','Forward'), ('backward','Backward')], string="Direction")
    start_date = fields.Datetime(string="Start Date")
    
class MarketingCampaignSegmentReverse(models.Model):

    _inherit = "marketing.campaign.segment"
    
    @api.v7
    @api.cr_uid_ids_context
    def process_segment(self, cr, uid, segment_ids=None, context=None):
        _logger.error("Process Segment Hack")
        Workitems = self.pool.get('marketing.campaign.workitem')
        Campaigns = self.pool.get('marketing.campaign')
        if not segment_ids:
            segment_ids = self.search(cr, uid, [('state', '=', 'running')], context=context)

        #action_date = time.strftime('%Y-%m-%d %H:%M:%S')

        
        campaigns = set()
        for segment in self.browse(cr, uid, segment_ids, context=context):
            if segment.campaign_id.state != 'running':
                continue

            if segment.campaign_id.direction == "backward":
                action_date = segment.campaign_id.start_date

            campaigns.add(segment.campaign_id.id)
            act_ids = self.pool.get('marketing.campaign.activity').search(cr,
                  uid, [('start', '=', True), ('campaign_id', '=', segment.campaign_id.id)], context=context)

            model_obj = self.pool[segment.object_id.model]
            criteria = []
            if segment.sync_last_date and segment.sync_mode != 'all':
                criteria += [(segment.sync_mode, '>', segment.sync_last_date)]
            if segment.ir_filter_id:
                criteria += eval(segment.ir_filter_id.domain)
            object_ids = model_obj.search(cr, uid, criteria, context=context)

            # XXX TODO: rewrite this loop more efficiently without doing 1 search per record!
            for record in model_obj.browse(cr, uid, object_ids, context=context):
                # avoid duplicate workitem for the same resource
                if segment.sync_mode in ('write_date','all'):
                    if Campaigns._find_duplicate_workitems(cr, uid, record, segment.campaign_id, context=context):
                        continue

                wi_vals = {
                    'segment_id': segment.id,
                    'date': action_date,
                    'state': 'todo',
                    'res_id': record.id
                }

                partner = self.pool.get('marketing.campaign')._get_partner_for(segment.campaign_id, record)
                if partner:
                    wi_vals['partner_id'] = partner.id

                for act_id in act_ids:
                    wi_vals['activity_id'] = act_id
                    Workitems.create(cr, uid, wi_vals, context=context)

            self.write(cr, uid, segment.id, {'sync_last_date':action_date}, context=context)
        Workitems.process_all(cr, uid, list(campaigns), context=context)
        return True
