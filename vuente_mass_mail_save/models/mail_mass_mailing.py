# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
import werkzeug
import json

from openerp import api, fields, models

class SaveMailMassMailing(models.Model):

    _inherit = "mail.mass_mailing"
    
    m_campaign_id = fields.Many2one('marketing.campaign', string="Marketing Campaign")
    
    @api.one
    def save_to_campaign(self):
        partner_model = self.env['ir.model'].search([('model','=','res.partner')])[0]
        self.env['mail.template'].create({'name': self.name + " Mail Template", 'model_id': partner_model.id, 'body_html': self.body_html, 'subject': self.name, 'email_from': self.email_from})