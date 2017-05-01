import openerp.http as http
import requests
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)
import openerp
import werkzeug
import base64
import json
import sys
from urlparse import urlparse
import ast
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
from urlparse import parse_qs

from openerp.exceptions import ValidationError

class QuickbooksController(http.Controller):

    @http.route('/quickbooks/oauth', type="http", auth="user")
    def quickbooks_oauth(self, **kwargs):
        
        values = {}
	for field_name, field_value in kwargs.items():
            values[field_name] = field_value

        oauth_verifier = values['oauth_verifier']

        quickbooks_account = request.env['migration.quickbooks'].search([('resource_owner_key','=', values['oauth_token'] )])
        
        oauth = OAuth1(quickbooks_account.oauth_consumer_key, client_secret=quickbooks_account.oauth_consumer_secret, resource_owner_key=quickbooks_account.resource_owner_key, resource_owner_secret=quickbooks_account.resource_owner_secret, verifier=oauth_verifier)

        access_token_url = "https://oauth.intuit.com/oauth/v1/get_access_token"
        r = requests.post(url=access_token_url, auth=oauth)
        credentials = parse_qs(r.content)
        request.env.user.quickbooks_oauth_access_token = credentials.get('oauth_token')[0]
        request.env.user.quickbooks_oauth_access_token_secret = credentials.get('oauth_token_secret')[0]
        request.env.user.quickbooks_realm_id = values['realmId']

	quickbooks_menu = request.env['ir.model.data'].get_object('migration_quickbooks_online', 'migration_quickbooks_menu')
	quickbooks_action = request.env['ir.model.data'].get_object('migration_quickbooks_online', 'migration_quickbooks_action')

        return werkzeug.utils.redirect( "/web#id=" + str(quickbooks_account.id) + "&view_type=form&model=migration.quickbooks&menu_id=" + str(quickbooks_menu.id) + "&action=" + str(quickbooks_action.id) )