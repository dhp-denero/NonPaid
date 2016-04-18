# -*- coding: utf-8 -*-
from openerp import api, fields, models

from openerp.http import request
from openerp.osv import osv

import requests
import werkzeug

class ProjectTaskUpload(models.Model):

    _inherit = "project.task"
    
    @api.one
    def upload_task_vuente(self):
        server_url = "http://www.vuente.com"
        #server_url = "http://192.168.56.109:8069"
        
        return_string = requests.get(server_url + "/upload/task?task_id=" + str(self.id) + "&task_name=" + self.name.encode("utf-8") + "&task_description=" + self.description.encode("utf-8") + "&task_host=" + request.httprequest.host_url)

        raise osv.except_osv(("Warning"), ("Your task has been uploaded and will be reviewed soon"))  