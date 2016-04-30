# -*- coding: utf-8 -*-
import werkzeug
import json
import base64
from datetime import datetime

import openerp.http as http
from openerp.http import request

from openerp.addons.website.models.website import slug

class SaasClientControllers(http.Controller):

    @http.route('/saas/client/login',type="http", auth="public", csrf=False)
    def saas_client_login(self, **kwargs):
        
        values = {}
	for field_name, field_value in kwargs.items():
            values[field_name] = field_value
        
        ref_url = ""
        if 'Referer' in http.request.httprequest.headers:
            ref_url = http.request.httprequest.headers['Referer']
            
        
        failed_logins = request.env['remote.login.log'].sudo().search_count([('user_name', '=', values['user'] ), ('create_date','>=',  datetime.utcnow().strftime("%Y-%m-%d 00:00:00") ), ('create_date','<=',  datetime.utcnow().strftime("%Y-%m-%d 23:59:59") ) ])

        if failed_logins >= 3:
            return "Max of " + str(failed_logins) + " has been exceeded"

        #Automatically sign the new user in
        #request.cr.commit()     # as authenticate will use its own cursor we need to commit the current transaction
	redirect_url = "/web"

	if request.session.authenticate(request.env.cr.dbname, values['user'], values['password']):
	    #Redirect to standard front page (sorry custom page not supported)
	    redirect_url = "/web"
	else:
	    #Failed login attempts gets logged and the user is redirected to the normal login
	    request.env['remote.login.log'].sudo().create({'user_name': values['user'], 'ref_url': ref_url})
            redirect_url = "/web/login"

        return werkzeug.utils.redirect(redirect_url)