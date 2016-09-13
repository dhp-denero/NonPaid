from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)
import datetime
 
class ProjectTaskReminder(models.Model):

    _inherit = "project.task"
    
    @api.model
    def send_email_reminder(self):
        #send an email out to everyone in the category
        notification_template = self.env['ir.model.data'].sudo().get_object('vuente_task_reminder', 'task_reminder')
        
        #Monday = 0, Sunday = 6
        day_of_week = datetime.datetime.today().weekday()
   
        for user in self.env['res.users'].search([]):
            task_list_string = ""
            working_today = False
            for task in user.task_ids:
                if task.stage_id.name != "Done":
                    
                    
                    for work_day in user.days_work:
                        if day_of_week == work_day.day_number:
                            working_today = True
                    
                    if working_today:
                        task_list_string += "<b>Project Name</b>: " + task.project_id.name + "<br/>\n"
                        task_list_string += "<b>Task Name</b>: " + task.name + "<br/>\n"
                    
                        task_list_string += "<b>Task Deadline</b>: "
                    
                        if task.date_deadline:
                            task_list_string += task.date_deadline + "<br/>\n"
                        else:
                            task_list_string += "<br/>\n"
                    
                        task_list_string += "<b>Task Stage</b>: " + task.stage_id.name + "<br/>\n"
                        task_list_string += "<b>Task Description</b>: <br/>\n"
                                
                        if task.description:
                            task_list_string += task.description + "<br/>\n"                
                
                        task_list_string += "<hr/>\n"

            if working_today:
                notification_template.body_html = notification_template.body_html.replace("_task_list_",  task_list_string)
                notification_template.send_mail(user.id, True)