# -*- coding: utf-8 -*-
from openerp import api, fields, models
import requests
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
import json

class MailMailSendgridAccount(models.Model):

    _name = "mail.mail.sendgrid.account"
    
    last_sync = fields.Datetime(string="Last Sync Date", default="2016-01-01 01:01:01")
    api_key = fields.Char(string="API Key")
    
    @api.model
    def check_sendgrid_stats(self):
        for account in self.env['mail.mail.sendgrid.account'].search([]):
            my_time = datetime.strptime(account.last_sync,'%Y-%m-%d %H:%M:%S')
	    start_date = str(my_time.strftime('%Y-%m-%d'))

            headers = {'Authorization': 'Bearer ' + account.api_key}

            response_string = requests.get("https://api.sendgrid.com/v3/stats?start_date=" + start_date, headers=headers)
	    account.last_sync = datetime.utcnow()
	    for stat_day in json.loads(response_string.text.encode('utf-8')):	            
	        if self.env['mail.mail.sendgrid.statistic'].search_count([('stat_date', '=', stat_day['date'])]) == 0:
	            self.env['mail.mail.sendgrid.statistic'].create({'stat_date': stat_day['date'], 'blocks': stat_day['stats'][0]['metrics']['blocks'], 'bounce_drops': stat_day['stats'][0]['metrics']['bounce_drops'], 'bounces': stat_day['stats'][0]['metrics']['bounces'], 'clicks': stat_day['stats'][0]['metrics']['clicks'], 'deferred': stat_day['stats'][0]['metrics']['deferred'], 'delivered': stat_day['stats'][0]['metrics']['delivered'], 'invalid_emails': stat_day['stats'][0]['metrics']['invalid_emails'], 'opens': stat_day['stats'][0]['metrics']['opens'], 'processed': stat_day['stats'][0]['metrics']['processed'], 'requests': stat_day['stats'][0]['metrics']['requests'], 'spam_report_drops': stat_day['stats'][0]['metrics']['spam_report_drops'], 'spam_reports': stat_day['stats'][0]['metrics']['spam_reports'], 'unique_opens': stat_day['stats'][0]['metrics']['unique_opens'], 'unsubscribe_drops': stat_day['stats'][0]['metrics']['unsubscribe_drops'], 'unsubscribes': stat_day['stats'][0]['metrics']['unsubscribes']})	        
	    
	