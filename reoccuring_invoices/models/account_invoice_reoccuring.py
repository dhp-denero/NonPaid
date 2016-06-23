# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
from datetime import datetime, timedelta
import time

from dateutil.relativedelta import relativedelta

from openerp import api, fields, models
import openerp.http as http
from openerp.http import request
import os
import openerp

class AccountInvoiceReoccuring(models.Model):

    _name = "account.invoice.reoccuring"
    
    partner_id = fields.Many2one('res.partner', string="Partner", required="True")
    plan_start_date = fields.Date(string="Plan Start Date", required="True")
    plan_frequency = fields.Selection([('months','Monthly')], string="Plan Frequency", default="months", required="True")
    next_invoice_date = fields.Date(string="Next Invoice Date")
    template_invoice = fields.Many2one('account.invoice', string="Template Invoice", required="True", domain="[('state','=','draft')]")
    invoice_history = fields.One2many('account.invoice.reoccuring.history','air_id', string="Invoice History")
    
    @api.onchange('plan_start_date')
    def _onchange_plan_start_date(self):
        if self.plan_start_date:
            self.next_invoice_date = datetime.strptime(self.plan_start_date,"%Y-%m-%d") + relativedelta(months=1)
        
    @api.model
    def invoice_members(self):
        invoice_partners = self.env['account.invoice.reoccuring'].search([('next_invoice_date', '<=', datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") )])
        
        for invoice_part in invoice_partners:
            #Create a new invoice
            invoice_email_template = self.env['ir.model.data'].get_object('account', 'email_template_edi_invoice')
            template_invoice = invoice_part.template_invoice
            
            new_invoice = template_invoice.copy()
            
            #Change the invoice so it to the partner
            new_invoice.partner_id = invoice_part.partner_id.id
            
            #Validate the invoice
            new_invoice.action_date_assign()
	    new_invoice.action_move_create()
            new_invoice.invoice_validate()

            #Add the invoice to the history
            self.env['account.invoice.reoccuring.history'].create({'air_id': invoice_part.id, 'invoice_id': new_invoice.id})
            
            #Email the invoice and pray they pay
            invoice_email_template.send_mail(new_invoice.id, True)
            
            #Set thier next invoice to be 30 from the previous invoice
            invoice_part.next_invoice_date = datetime.strptime(invoice_part.next_invoice_date,"%Y-%m-%d") + relativedelta(months=1)
                        
class AccountInvoiceReoccuringHistory(models.Model):

    _name = "account.invoice.reoccuring.history"
    
    air_id = fields.Many2one('account.invoice.reoccuring', string="Reoccuring Invoice")
    invoice_id = fields.Many2one('account.invoice', string="Invoice")

