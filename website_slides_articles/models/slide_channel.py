# -*- coding: utf-8 -*-
from openerp import api, fields, models

class SlideChannelCategory(models.Model):

    _inherit = "slide.channel"
    
    blog_tag_id = fields.Many2one('blog.blog', string="Blog Category")
    slide_blog_url = fields.Char(string="Blog URL", compute="_compute_bu_url")
    channel_category_id = fields.Many2one('vuente.slide.channel.category', string="Vuente Channel Category")
    
    @api.one
    @api.depends('name')
    def _compute_bu_url(self):
        if self.blog_tag_id:
            self.slide_blog_url = self.blog_tag_id.name.replace(" ","-").lower()
            self.slide_blog_url += "-" + str(self.blog_tag_id.id)
        else:
            slide_blog_url = "blog"
            
class SlideChannelMasterCategory(models.Model):

    _name = "vuente.slide.channel.category"
    
    name = fields.Char(string="Name")
