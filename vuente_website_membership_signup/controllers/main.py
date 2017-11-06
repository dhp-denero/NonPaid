# -*- coding: utf-8 -*-
import werkzeug
import json
import base64

import openerp.http as http
from openerp.http import request

from openerp.addons.website.models.website import slug

class WebsiteMembershipSignup(http.Controller):

    @http.route('/website/membership/signup/<membership_id>', type="http", auth="public", website=True)
    def website_membership_signup(self, membership_id, **kw):
        """Displays a signup form for the memerbship level"""
        
        membership = request.env['product.template'].browse( int(membership_id) )
        
        #Only display membership products(prevent people from scouting all products)
        if membership.membership:
            return http.request.render('vuente_website_membership_signup.membership_signup_form', {'membership': membership})
            
    @http.route('/site/membership/signup/process', type="http", auth="public", website=True, csrf=False)
    def website_membership_signup_process(self, **kwargs):
        
        values = {}
	for field_name, field_value in kwargs.items():
	    values[field_name] = field_value
	    
	membership = request.env['product.template'].browse( int(values['membership_id']) )
	
	#Create the new user
	new_user = request.env['res.users'].sudo().create({'name': values['name'], 'login': values['email'], 'email': values['email'], 'password': values['password'] })
	
	#Add the user to the assigned groups
	for user_group in membership.signup_group_ids:
            user_group.users = [(4, new_user.id)]

        #Remove 'Contact Creation' permission        
	contact_creation_group = request.env['ir.model.data'].sudo().get_object('base', 'group_partner_manager')
        contact_creation_group.users = [(3,new_user.id)]

        #Add them as a portal user
	portal_group = request.env['ir.model.data'].sudo().get_object('base', 'group_portal')
        portal_group.users = [(4,new_user.id)]

        #Also remove them as an employee
	human_resources_group = request.env['ir.model.data'].sudo().get_object('base', 'group_user')
        human_resources_group.users = [(3,new_user.id)]

        #Modify the users partner record
        extra_fields_dict = {}
        for extra_field in membership.extra_fields:
	    extra_fields_dict[extra_field.name] = values[extra_field.name]
	
	new_user.partner_id.write(extra_fields_dict)

        #Automatically sign the new user in
        request.cr.commit()     # as authenticate will use its own cursor we need to commit the current transaction
	request.session.authenticate(request.env.cr.dbname, values['email'], values['password'])

        order = request.website.sale_get_order(force_create=1)
        cart_values = order._cart_update(product_id=membership.id, add_qty=1)

        #Redirect them to thier profile page
        return werkzeug.utils.redirect("/shop/checkout")
