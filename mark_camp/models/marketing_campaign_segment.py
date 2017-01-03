# -*- coding: utf-8 -*-
from openerp import api, fields, models, tools
import logging
_logger = logging.getLogger(__name__)
import ast
from openerp.exceptions import UserError
from openerp.osv import osv

class MarkCampSeg(models.Model):

    _inherit = "marketing.campaign.segment"
    
    filter_count = fields.Integer(string='Filter Count')
    ir_filter_id = fields.Many2one('ir.filters', required=True)
    
    @api.one
    @api.onchange('ir_filter_id')
    def _onchange_filter(self):
        if self.campaign_id and self.ir_filter_id.domain:
            _logger.error(self.ir_filter_id.domain)
            _logger.error(self.campaign_id.object_id.model)
            
            my_filter = ast.literal_eval(self.ir_filter_id.domain)
            
            if self.ir_filter_id.domain == "[]":
                self.ir_filter_id = ""
                #raise osv.except_osv(("Warning"), ("Using a filter that matches everyone is unsafe!"))            

                
            self.filter_count = self.env[str(self.campaign_id.object_id.model)].search_count(my_filter)
