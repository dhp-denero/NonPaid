# -*- coding: utf-8 -*-
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class CalendarAlarmDefaults(models.Model):

    _inherit = "calendar.alarm"

    @api.model
    def _default_sms_template_id(self):
        default_email_template_id = self.env['ir.model.data'].get_object('sms_frame_calendar_alarm','sms_calendar_reminder')
        return default_email_template_id
    
    mail_template_id = fields.Many2one('mail.template')
    sms_template_id = fields.Many2one('sms.template', default=_default_sms_template_id)
