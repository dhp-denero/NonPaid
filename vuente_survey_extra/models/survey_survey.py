# -*- coding: utf-8 -*-
from openerp import api, fields, models

class SurveySurveyLeads(models.Model):

    _inherit = "survey.survey"
    
    lead_survey = fields.Boolean(string="Lead Survey")