# -*- coding: utf-8 -*-
from datetime import datetime

from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MarketingCampaignActivityTask(models.Model):

    _inherit = "marketing.campaign.activity"
    
    type = fields.Selection(selection_add=[('task','Task')])
    task_template_id = fields.Many2one('task.template', string="Task Template")
    vuente_from_email = fields.Char(string="From Email")
    vuente_mail_server = fields.Many2one('ir.mail_server', string="Mail Server")
    vuente_reply_to = fields.Char(string="Reply To")
    
    @api.model
    def _process_wi_task(self, activity, workitem):
        _logger.error("create task")
        task_template = self.env['task.template'].browse(activity.task_template_id.id)
        new_task = self.env['project.task'].create({'name': task_template.name, 'department_id': task_template.department_id.id, 'description': task_template.description})
        
        _logger.error("created email")
        #Send an email out to everyone in the department notifying them of the new task
        notification_template = self.env['ir.model.data'].get_object('vuente_automated_task_tunnels', 'new_department_task')
       	       
       	notification_template.body_html = notification_template.body_html.replace("__task_name__", new_task.name)
       	notification_template.body_html = notification_template.body_html.replace("__task_description__", new_task.description)
       	notification_template.body_html = notification_template.body_html.replace("__department__", new_task.department_id.name)

       	_logger.error(notification_template.body_html)
       	
        for employee in new_task.department_id.employee_ids:
            _logger.error(employee.name)
            notification_template.send_mail(employee.id, True)
        