# -*- coding: utf-8 -*-
from openerp import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class UnfinishedTasks(models.Model):

    _inherit = "project.project"
    
    @api.model
    def check_all_tasks(self):
        _logger.error("uft")
        #Send an email out to everyone in the department notifying them of the new task
        notification_template = self.env['ir.model.data'].get_object('vuente_unfinished_tasks', 'unfinished_tasks')
       	       
        for project in self.env['project.project'].search([]):
            _logger.error(project.name)
            task_list_string = ""
            task_list_string += "<table>\n<tr><td>Name</td><td>Description</td><td>Stage</td></tr>\n"

            for task in project.task_ids.search([('stage_id.name','!=','Done')]):
               task_list_string += "<tr><td>" + str(task.name) + "</td><td>" + str(task.description) + "</td><td>" + str(task.stage_id.name) + "</td></tr>\n"
            
            task_list_string += "</table>\n"
            
            notification_template.body_html = notification_template.body_html.replace("__task_list__", task_list_string)
            notification_template.send_mail(project.id, True)        
            _logger.error(notification_template.body_html)