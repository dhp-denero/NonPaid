# -*- coding: utf-8 -*-
from openerp.http import request
import requests
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import logging
_logger = logging.getLogger(__name__)
import json
from openerp import api, fields, models
from openerp.exceptions import ValidationError, UserError
import base64
from lxml import html, etree
from random import randint
import time
from datetime import datetime

class MigrationQuickbooks(models.Model):

    _name = "migration.quickbooks"

    name = fields.Char(string="Name")
    oauth_consumer_key = fields.Char(string="OAuth Consumer Key")
    oauth_consumer_secret = fields.Char(string="OAuth Consumer Secret")
    resource_owner_key = fields.Char(string="Resource Owner Key")
    resource_owner_secret = fields.Char(string="Resource Owner Secret")
    
    @api.multi
    def auth_quickbooks(self):
        self.ensure_one()

        request_token_url = "https://oauth.intuit.com/oauth/v1/get_request_token"
        data_dict = {}
        data_dict['oauth_callback'] = request.httprequest.host_url + "quickbooks/oauth"

        oauth = OAuth1(self.oauth_consumer_key, client_secret=self.oauth_consumer_secret)
        r = requests.post(url=request_token_url, data=data_dict, auth=oauth)

        credentials = parse_qs(r.content)
        self.resource_owner_key = credentials.get('oauth_token')[0]
        self.resource_owner_secret = credentials.get('oauth_token_secret')[0]

        base_authorization_url = "https://appcenter.intuit.com/Connect/Begin"
        authorization_url = base_authorization_url + '?oauth_token=' + self.resource_owner_key

        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': authorization_url
        }
        
        #Ask for token
        #headers_dict = {}
        #headers_dict['oauth_callback'] = "http://google.com.au"
        #headers_dict['oauth_consumer_key'] = self.oauth_consumer_key
        #headers_dict['oauth_nonce'] = randint(1000000,9000000)
        #headers_dict['oauth_signature_method'] = "HMAC-SHA1"
        #headers_dict['oauth_timestamp'] = time.time()
        #headers_dict['auth_version'] = "1.0"
        #headers_dict['oauth_signature'] = self.generate_oauth_signature(headers_dict)
        
        #response_string = requests.get("https://oauth.intuit.com/oauth/v1/get_request_token", params=headers_dict)
        #raise UserError(response_string.text)

    @api.one
    def import_invoices(self):
        url = "https://quickbooks.api.intuit.com/v3/company/" + self.env.user.quickbooks_realm_id + "/query?query=" + "select * from Invoice"

        header = {'Accept': 'application/json'}
        oauth = OAuth1(self.oauth_consumer_key, client_secret=self.oauth_consumer_secret, resource_owner_key=self.env.user.quickbooks_oauth_access_token, resource_owner_secret=self.env.user.quickbooks_oauth_access_token_secret)
        r = requests.post(url=url, auth=oauth, headers=header)

        json_ob = json.loads(r.text)

        for invoice in json_ob['QueryResponse']['Invoice']:
            create_dict = {}                        

            if "CustomerRef" in invoice:
                quickbooks_customer = self.env['ir.model.data'].xmlid_to_object('quickbooks_import.import_customer_' + invoice['CustomerRef']['value'])
                create_dict['partner_id'] = quickbooks_customer.id

            if "CustomerMemo" in invoice:
                create_dict['comment'] = invoice['CustomerMemo']['value']

            if "DueDate" in invoice:
                create_dict['date_due'] = invoice['DueDate']            

            #Create an external ID so we don't reimport the same invoice again
            external_identifier = "import_invoice_" + str( invoice['Id'] )
            quickbooks_invoice = self.env['ir.model.data'].xmlid_to_object('quickbooks_import.' + external_identifier)
            invoice_account = self.env['account.account'].search([('user_type_id', '=', self.env.ref('account.data_account_type_receivable').id)], limit=1)

            if quickbooks_invoice:
                quickbooks_invoice.write(create_dict)
                
                #Remove all current lines so we can reimport them
                for invoice_line in quickbooks_invoice.invoice_line_ids:
                    invoice_line.unlink()

                if "Line" in invoice:
                    for invoice_line in invoice['Line']:
                        if "Id" in invoice_line:
                            invoice_line_dict = {'invoice_id': quickbooks_invoice.id, 'account_id': invoice_account.id, 'name': invoice_line['Description'], 'price_unit': invoice_line['SalesItemLineDetail']['UnitPrice'], 'quantity': invoice_line['SalesItemLineDetail']['Qty'] }
                            quickbooks_invoice_line = self.env['account.invoice.line'].create(invoice_line_dict)

            else:
                
                create_dict['type']  = 'out_invoice'
                create_dict['account_id'] = invoice_account.id
                        
                quickbooks_invoice = self.env['account.invoice'].create(create_dict)
                self.env['ir.model.data'].create({'module': "quickbooks_import", 'name': external_identifier, 'model': 'account.invoice', 'res_id': quickbooks_invoice.id })            

                if "Line" in invoice:
                    for invoice_line in invoice['Line']:
                        if "Id" in invoice_line:
                            invoice_line_dict = {'invoice_id': quickbooks_invoice.id, 'account_id': invoice_account.id, 'name': invoice_line['Description'], 'price_unit': invoice_line['SalesItemLineDetail']['UnitPrice'], 'quantity': invoice_line['SalesItemLineDetail']['Qty'] }
                            quickbooks_invoice_line = self.env['account.invoice.line'].create(invoice_line_dict)                            
                            
                            #Don't create the external ID, when the invoice gets deleted these seem to linger around
                            #self.env['ir.model.data'].create({'module': "quickbooks_import", 'name': "import_invoice_line_" + str( invoice_line['Id'] ), 'model': 'account.invoice.line', 'res_id': quickbooks_invoice_line.id })

            
    @api.one
    def import_customers(self):

        url = "https://quickbooks.api.intuit.com/v3/company/" + self.env.user.quickbooks_realm_id + "/query?query=" + "select * from Customer"
        
        header = {'Accept': 'application/json'}
        oauth = OAuth1(self.oauth_consumer_key, client_secret=self.oauth_consumer_secret, resource_owner_key=self.env.user.quickbooks_oauth_access_token, resource_owner_secret=self.env.user.quickbooks_oauth_access_token_secret)
        r = requests.post(url=url, auth=oauth, headers=header)

        json_ob = json.loads(r.text)

        for customer in json_ob['QueryResponse']['Customer']:
            create_dict = {}

            if "BillAddr" in customer:
                if "Line1" in customer['BillAddr']:
                    create_dict['street'] = customer['BillAddr']['Line1']

                if "City" in customer['BillAddr']:
                    create_dict['city'] = customer['BillAddr']['City']

                if "Country" in customer['BillAddr']:
                    country = self.env['res.country'].search([('name','=',customer['BillAddr']['Country'])])
                    if country:
                        create_dict['country_id'] = country.id

                if "CountrySubDivisionCode" in customer['BillAddr']:
                    state = self.env['res.country.state'].search([('name','=',customer['BillAddr']['CountrySubDivisionCode'])])
                    if state:
                        create_dict['state_id'] = state.id

                if "PostalCode" in customer['BillAddr']:
                    create_dict['zip'] = customer['BillAddr']['PostalCode']

            if "Notes" in customer:
                create_dict['comment'] = customer['Notes']

            create_dict['name'] = customer['DisplayName']

            if "PrimaryPhone" in customer:
                create_dict['phone'] = customer['PrimaryPhone']['FreeFormNumber']

            if "Mobile" in customer:
                create_dict['mobile'] = customer['Mobile']['FreeFormNumber']

            if "Fax" in customer:
                create_dict['fax'] = customer['Fax']['FreeFormNumber']

            if "PrimaryEmailAddr" in customer:
                create_dict['email'] = customer['PrimaryEmailAddr']['Address']

            if "WebAddr" in customer:
                create_dict['website'] = customer['WebAddr']['URI']

            #Create an external ID so we don't reimport the same customer again
            external_identifier = "import_customer_" + str( customer['Id'] )
            quickbooks_customer = self.env['ir.model.data'].xmlid_to_object('quickbooks_import.' + external_identifier)
            if quickbooks_customer:
                quickbooks_customer.write(create_dict)
            else:
                create_dict['customer'] = True
                quickbooks_customer = self.env['res.partner'].create(create_dict)
                self.env['ir.model.data'].create({'module': "quickbooks_import", 'name': external_identifier, 'model': 'res.partner', 'res_id': quickbooks_customer.id })            

                
    @api.one
    def import_employees(self):

        url = "https://quickbooks.api.intuit.com/v3/company/" + self.env.user.quickbooks_realm_id + "/query?query=" + "select * from Employee"
        
        header = {'Accept': 'application/json'}
        oauth = OAuth1(self.oauth_consumer_key, client_secret=self.oauth_consumer_secret, resource_owner_key=self.env.user.quickbooks_oauth_access_token, resource_owner_secret=self.env.user.quickbooks_oauth_access_token_secret)
        r = requests.post(url=url, auth=oauth, headers=header)

        json_ob = json.loads(r.text)
            
        for employee in json_ob['QueryResponse']['Employee']:

            create_dict = {}
            create_dict['name'] = employee['DisplayName']

            if "Gender" in employee:            
                create_dict['gender'] = employee['Gender'].lower()
            
            if "PrimaryEmailAddr" in employee:
                create_dict['work_email'] = employee['PrimaryEmailAddr']['Address']
            
            if "PrimaryPhone" in employee:
                create_dict['work_phone'] = employee['PrimaryPhone']['FreeFormNumber']

            if "Mobile" in employee:            
                create_dict['mobile_phone'] = employee['Mobile']['FreeFormNumber']

            if "BirthDate" in employee:
                create_dict['birthday'] = employee['BirthDate']

            if "EmployeeNumber" in employee:            
                create_dict['identification_id'] = employee['EmployeeNumber']

            #Create an external ID so we don't reimport the same employee again
            external_identifier = "import_employee_" + str( employee['Id'] )
            quickbooks_employee = self.env['ir.model.data'].xmlid_to_object('quickbooks_import.' + external_identifier)
            if quickbooks_employee:
                quickbooks_employee.write(create_dict)
            else:
                quickbooks_employee = self.env['hr.employee'].create(create_dict)
                self.env['ir.model.data'].create({'module': "quickbooks_import", 'name': external_identifier, 'model': 'hr.employee', 'res_id': quickbooks_employee.id })            

