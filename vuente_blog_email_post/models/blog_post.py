# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class BlogPostEmail(models.Model):

    _inherit = 'blog.post'
    
    def message_new(self, msg, custom_values=None):
        """ Override to post new blog post according to the email. """

        if custom_values is None:
            custom_values = {}
        
        message_body = "<div class=\"container\">" + msg.get('body').encode("utf-8") + "</div>"
        defaults = {
            'name': msg.get('subject') or "No Subject",
            'blog_id': 1,
            'content': message_body,
            'website_published': True,
        }

        defaults.update(custom_values)
        
        return super(BlogPostEmail, self).message_new(msg, custom_values=defaults)