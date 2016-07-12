# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class ResPartner(models.Model):

    _inherit = "res.partner"
    
    email_tracking_sent = fields.Integer(string="Emails Sent", compute='_compute_email_tracking_sent')
    email_tracking_opened = fields.Integer(string="Emails Opened", compute='_compute_email_tracking_opened')

    @api.one
    def _compute_email_tracking_sent(self):
        self.email_tracking_sent = self.env['mail.mail.statistics'].search_count([('my_partner','=',self.id), ('sent','!=', False)])

    @api.one        
    def _compute_email_tracking_opened(self):
        self.email_tracking_opened = self.env['mail.mail.statistics'].search_count([('my_partner','=',self.id), ('opened','!=', False)])
        
    @api.multi
    def open_mail_sent(self):
        self.ensure_one()
        return {
            'name': 'Partner Mail Sent Stats',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mail.mail.statistics',
            'views': [(self.env.ref('vuente_mail_tracking.res_partner_track_stats_view_tree').id,'tree')],
            'type': 'ir.actions.act_window',
            'domain': [('sent','!=',False), ('my_partner','=', self.id)],
        }
        
    @api.multi
    def open_mail_opened(self):
        self.ensure_one()
        return {
            'name': 'Partner Mail Opened Stats',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mail.mail.statistics',
            'views': [(self.env.ref('vuente_mail_tracking.res_partner_track_stats_view_tree').id,'tree')],
            'type': 'ir.actions.act_window',
            'domain': [('opened','!=',False), ('my_partner','=', self.id)],
        }
