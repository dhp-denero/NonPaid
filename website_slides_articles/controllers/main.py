# -*- coding: utf-8 -*-
import werkzeug
import json
import base64
from datetime import datetime

from openerp.addons.web import http
from openerp.http import request

from openerp.addons.website.models.website import slug

class VuenteSlideChannelCategoriesControllers(http.Controller):

    @http.route('/slides/channel/category/<channel_id>',type="http", auth="public", website=True, csrf=False)
    def vuente_channel_category(self, channel_id, **kwargs):
        
        vuente_category = request.env['vuente.slide.channel.category'].browse( int(channel_id) )
        channels = request.env['slide.channel'].search([('channel_category_id','=', int(channel_id) )], order='sequence, id')
	
	return request.website.render('website_slides_articles.vuente_channel_categories', {
	            'channels': channels,
	            'user': request.env.user,
	            'is_public_user': request.env.user == request.website.user_id,
	            'vuente_category': vuente_category.name
        })