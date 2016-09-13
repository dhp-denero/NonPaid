from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class ResUsersTaskReminder(models.Model):

    _inherit = "res.users"
    
    task_ids = fields.One2many('project.task', 'user_id', string="Tasks")
    days_work = fields.Many2many('res.users.work', string="Work Days")

class ResUsersTaskReminderWorkDays(models.Model):

    _name = "res.users.work"
    
    day_number = fields.Integer(string="Day Number")
    name = fields.Char(string="Name")