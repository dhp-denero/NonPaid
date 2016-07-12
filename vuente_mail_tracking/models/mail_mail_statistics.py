# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class MailMailStatisticsCampaign(models.Model):

    _inherit = "mail.mail.statistics"
    
    marketing_campaign_id = fields.Many2one('marketing.campaign', string="Marketing Campaign")
    mail_template_id = fields.Many2one('mail.template', string="Mail Template")
    my_partner = fields.Many2one('res.partner', string="My Partner", compute="_compute_my_partner")
    
    @api.one
    @api.depends('model','res_id')
    def _compute_my_partner(self):
        #my_model = self.env['ir.model'].sudo().browse(self.model)
        my_model = self.env['ir.model'].sudo().search([('id','=',self.model)])[0]
        
        if my_model.model == "res.partner":
            self.my_partner = self.env['res.partner'].sudo().browse(self.res_id)