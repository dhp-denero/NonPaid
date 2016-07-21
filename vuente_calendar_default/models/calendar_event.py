# -*- coding: utf-8 -*-
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class CalendarEventAlarmDefaults(models.Model):

    _inherit = "calendar.event"

    @api.model
    def _default_calendar_reminder_defaults_ids(self):
        default_alarms = self.env['ir.config_parameter'].get_param('default_calendar_alarms')

        return self.env['calendar.alarm'].search([('id', 'in', default_alarms.split(";") )])
    
    alarm_ids = fields.Many2many('calendar.alarm', default=_default_calendar_reminder_defaults_ids)