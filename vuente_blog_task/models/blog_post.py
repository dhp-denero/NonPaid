# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class BlogPostTask(models.Model):

    _inherit = 'blog.post'
    
    @api.one
    def create_task_from_blog(self):
        self.env['project.task'].sudo().create({'name': self.name})