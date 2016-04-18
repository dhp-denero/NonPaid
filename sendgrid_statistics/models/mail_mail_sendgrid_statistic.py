# -*- coding: utf-8 -*-
from openerp import api, fields, models

class MailMailSendgridStatistic(models.Model):

    _name = "mail.mail.sendgrid.statistic"
    
    stat_date = fields.Date(readonly=True, string="Stat Date")
    blocks = fields.Integer(string="Blocks")
    bounce_drops = fields.Integer(string="Bounce Drops")
    bounces = fields.Integer(string="Bounces")
    clicks = fields.Integer(string="Cllicks")
    deferred = fields.Integer(string="Deferred")
    delivered = fields.Integer(string="Delivered")
    invalid_emails = fields.Integer(string="Invalid Emails")
    opens = fields.Integer(string="Opens")
    processed = fields.Integer(string="Processed")
    requests = fields.Integer(string="Requests")
    spam_report_drops = fields.Integer(string="Spam Report Drops")
    spam_reports = fields.Integer(string="Spam Reports")
    unique_opens = fields.Integer(string="Unique Opens")
    unsubscribe_drops = fields.Integer(string="Unsubscribe Drops")
    unsubscribes = fields.Integer(string="Unsubscribes")
