# -*- coding: utf-8 -*-
from datetime import datetime

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)
from traceback import format_exception
from sys import exc_info

DT_FMT = '%Y-%m-%d %H:%M:%S'

class MarketingCampaignWorkitem(models.Model):

    _inherit = "marketing.campaign.workitem"
    
    testid = fields.Integer(string="Test ID")
    
    @api.one
    def vuente_test_process(self):
        if self.state != 'todo':
            return False

        activity = self.activity_id
        
        try:
            result = activity.process(activity.id, self.id)
        
            values = dict(state='done')
            if not self.date:
                values['date'] = datetime.now().strftime(DT_FMT)
            self.write(values)
            
        except Exception:
            tb = "".join(format_exception(*exc_info()))
            self.write({'state': 'exception', 'error_msg': tb})        
    