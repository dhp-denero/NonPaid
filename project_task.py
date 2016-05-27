# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteOurModuleProjectTask(models.Model):

    _inherit = "project.task"

    custom_field_1 = fields.Text(string="1 Subject Line and Reference URL")
    custom_field_2 = fields.Text(string="2 Short story and intro")
    custom_field_3 = fields.Text(string="3 Has a space between like Anthony writes")
    custom_field_4 = fields.Text(string="4 If Required")
    custom_field_5 = fields.Text(string="5 If Required")
	custom_field_6 = fields.Text(string="6 If Required")
    custom_field_7 = fields.Text(string="7 Call To Action and URL link to submit")

