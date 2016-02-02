# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteCrmLead(models.Model):

  _inherit = "crm.lead"

  first_name = fields.Char(string="First Name", size=50)
  last_name = fields.Char(string="Last Name", size=50)        