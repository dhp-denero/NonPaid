# -*- coding: utf-8 -*-
from openerp import api, fields, models, tools

class MarkCamp(models.Model):

    _name = "mark.camp"
    
    name = fields.Char(required=True, string='Name')
    model = fields.Selection(( ('res.partner','Partner'), ('crm.lead','Lead') ), default="res.partner", string='Resource', help="Which part of your system the contacts are drawn from")
    filter_ids = fields.One2many('mark.camp.filter', 'mc_id', string="Database Segments", required=True, help="Define the section of your contact list that will automaticly get put on this campaign")
    activity_ids = fields.One2many('mark.camp.activity', 'mc_id', required=True, string="Activites", help="List of emails / other activities that are executed as part of this campaign")
    state = fields.Selection([('draft','Draft'), ('running','Running'), ('done','Done')], string="State", default="draft")
    
class MarkCampFilter(models.Model):

    _name = "mark.camp.filter"    
    
    mc_id = fields.Many2one('mark.camp', string="Marketing Campaign")
    model = fields.Char(string="Model")
    filter_id = fields.Many2one('ir.filters', string="Filter", help="The section of your contacts that this campaign applies to")
    filter_count = fields.Integer(string="Filter Count", readonly=True, help="The amount of people that currently match this campaign")
    
#    @api.one
#    @api.onchange('filter_id')
#    def _onchange_filter_id(self):
        #count the amount of records that match this filter
#        if self.filter_id:
#            self.filter_count = self.env[self.model].search_count(self.filter_id.domain)
    
class MarkCampActivity(models.Model):

    _name = "mark.camp.activity"

    mc_id = fields.Many2one('mark.camp', string="Marketing Campaign")
    model = fields.Char(string="Model")
    name = fields.Char(required=True, string="Name")
    start = fields.Boolean(string="Start", help="Should this activity execute when the user enters the campaign?")
    type = fields.Selection([('email','Email')], string="Type", default="email")
    email_template_id = fields.Many2one('mail.template', string="Email Template")
    delay_unit = fields.Selection( [('minutes','Minutes'),('hours','Hours'), ('days','Days')], string="Delay Unit", default="days")
    delay = fields.Integer(string="Delay", help="The amount of time before the next email is sent", default="1")