# -*- coding: utf-8 -*-
from openerp import api, fields, models, tools

class SlideChannelImage(models.Model):

    _inherit = "slide.channel"
    
    image = fields.Binary(string="Image")