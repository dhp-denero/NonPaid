# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class MailTemplateTracking(models.Model):

    _inherit = "mail.template"
    
    email_tracking_sent = fields.Integer(string="Emails Sent", compute='_compute_email_tracking_sent')
    email_tracking_opened = fields.Integer(string="Emails Opened", compute='_compute_email_tracking_opened')

    @api.one
    def _compute_email_tracking_sent(self):
        self.email_tracking_sent = self.env['mail.mail.statistics'].search_count([('mail_template_id','=',self.id), ('sent','!=', False)])
        
    @api.one
    def _compute_email_tracking_opened(self):
        self.email_tracking_opened = self.env['mail.mail.statistics'].search_count([('mail_template_id','=',self.id), ('opened','!=', False)])

    @api.multi
    def open_mail_sent(self):
        self.ensure_one()
        return {
            'name': 'Email Template Mail Sent Stats',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mail.mail.statistics',
            'views': [(self.env.ref('vuente_mail_tracking.email_template_track_stats_view_tree').id,'tree')],
            'type': 'ir.actions.act_window',
            'domain': [('sent','!=',False), ('mail_template_id','=', self.id)],
        }
        
    @api.multi
    def open_mail_opened(self):
        self.ensure_one()
        return {
            'name': 'Email Template Mail Opened Stats',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mail.mail.statistics',
            'views': [(self.env.ref('vuente_mail_tracking.email_template_track_stats_view_tree').id,'tree')],
            'type': 'ir.actions.act_window',
            'domain': [('opened','!=',False), ('mail_template_id','=', self.id)],
        }
    
    @api.multi
    def send_mail_track(self, res_id, campaign_id, force_send=False, raise_exception=False):
        """Generates a new mail message for the given template and record,
           and schedules it for delivery through the ``mail`` module's scheduler.

           :param int res_id: id of the record to render the template with
                              (model is taken from the template)
           :param bool force_send: if True, the generated mail.message is
                immediately sent after being created, as if the scheduler
                was executed for this message only.
           :returns: id of the mail.message that was created
        """

        self.ensure_one()

        _logger.error("track template")
        Mail = self.env['mail.mail']
        Attachment = self.env['ir.attachment']  # TDE FIXME: should remove dfeault_type from context

        # create a mail_mail based on values, without attachments
        values = self.generate_email(res_id)
        values['recipient_ids'] = [(4, pid) for pid in values.get('partner_ids', list())]
        attachment_ids = values.pop('attachment_ids', [])
        attachments = values.pop('attachments', [])
        # add a protection against void email_from
        if 'email_from' in values and not values.get('email_from'):
            values.pop('email_from')


        #Add Tracking Hack Code
        values['statistics_ids'] = [(0, 0, {'model': self.model_id.id, 'res_id': res_id, 'marketing_campaign_id': campaign_id, 'mail_template_id': self.id})]

        mail = Mail.create(values)

        # manage attachments
        for attachment in attachments:
            attachment_data = {
                'name': attachment[0],
                'datas_fname': attachment[0],
                'datas': attachment[1],
                'res_model': 'mail.message',
                'res_id': mail.mail_message_id.id,
            }
            attachment_ids.append(Attachment.create(attachment_data).id)
        if attachment_ids:
            values['attachment_ids'] = [(6, 0, attachment_ids)]
            mail.write({'attachment_ids': [(6, 0, attachment_ids)]})

        if force_send:
            mail.send(raise_exception=raise_exception)
        return mail.id  # TDE CLEANME: return mail + api.returns ?