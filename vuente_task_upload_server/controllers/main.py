import openerp.http as http
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)
import werkzeug
import base64
import json
import openerp
import re

from openerp.addons.website.models.website import slug

class UploadTaskController(http.Controller):

    @http.route('/upload/task', website=True, type='http', auth="public")
    def upload_task(self, **kw):
        _logger.error("Upload Task")
        values = {}
	for field_name, field_value in kw.items():
            values[field_name] = field_value
        
        if request.env['project.task'].sudo().search_count([('remote_task_id','=', values['task_id']) ]) == 0:
            request.env['project.task'].sudo().create({'name': values['task_name'] + " (Remote)", 'description':values['task_description'], 'remote_task_id': values['task_id'], 'remote_task_host': values['task_host'], 'remote_task_url': values['task_host'] + "web?id=" + values['task_id'] + "&view_type=form&model=project.task" })
        
        return request.redirect("/upload/task/thankyou")

    @http.route('/upload/task/thankyou', website=True, type='http', auth="public")
    def upload_task_thankyou(self, **kw):
        return http.request.render('vuente_upload_server.task_upload_thankyou', {})
        