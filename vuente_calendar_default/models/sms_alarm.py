# -*- coding: utf-8 -*-
from datetime import datetime
from urllib import urlencode, quote as quote
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models, tools

class SMSAlarmVuente(models.Model):

    _inherit = "sms.alarm"
    
    @api.model        
    def send_sms_to_attendees(self,event,alarm):
        _logger.error("sms alarm vuente")
        sms_template = alarm.sms_template_id
        for attendee in event.partner_ids:
            _logger.error(attendee.mobile)
            _logger.error(sms_template.id)
            sms_template.sms_to = attendee.mobile
            self.env['sms.template'].send_sms(sms_template.id, event.id)