# -*- coding: utf-8 -*-
from openerp import api, fields, models

from openerp.http import request
from openerp.osv import osv

import requests
import werkzeug
import logging
_logger = logging.getLogger(__name__)

class ProjectTaskUpload(models.Model):

    _inherit = "project.task"
    
    @api.one
    def upload_task_vuente(self):
        server_url = "http://www.vuente.com"
        #server_url = "http://192.168.56.109:8069"
        _logger.error( str(self.id) )
        _logger.error( self.name.encode("utf-8") )
        _logger.error( self.description.encode("utf-8") )
        _logger.error( request.httprequest.host_url.encode("utf-8") )
        
        return_string = requests.get(server_url + "/upload/task?task_id=" + str(self.id) + "&task_name=" + self.name.encode("utf-8") + "&task_description=" + self.description.encode("utf-8") + "&task_host=" + request.httprequest.host_url.encode("utf-8") )

        raise osv.except_osv(("Warning"), ("Your task has been uploaded and will be reviewed soon"))  