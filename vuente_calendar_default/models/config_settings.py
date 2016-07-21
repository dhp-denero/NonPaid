# -*- coding: utf-8 -*-
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class ConfigSettingsGoogleContacts(models.TransientModel):

    _inherit = "base.config.settings"

    @api.model
    def _default_calendar_reminder_defaults_ids(self):
        default_alarms = self.env['ir.config_parameter'].get_param('default_calendar_alarms')

        return self.env['calendar.alarm'].search([('id', 'in', default_alarms.split(";") )])
    
    calendar_reminder_defaults_ids = fields.Many2many('calendar.alarm', string="Default Alarms", default=_default_calendar_reminder_defaults_ids)

    @api.model
    def set_calendar_reminder_defaults_ids(self, ids):
        ir_config_param = self.env['ir.config_parameter']
        config = self.browse(ids[0])
        alarms = config.calendar_reminder_defaults_ids
        alarm_string = ""
        for alarm in alarms:
            alarm_string += str(alarm.id) + ";"
            
        alarm_string = alarm_string[:-1]
        ir_config_param.set_param('default_calendar_alarms', alarm_string, groups=['base.group_system'])