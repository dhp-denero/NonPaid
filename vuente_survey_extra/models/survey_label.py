# -*- coding: utf-8 -*-
from openerp import api, fields, models

class SurveyLabelConditional(models.Model):

    _inherit = "survey.label"
    
    conditional_question_ids = fields.One2many('survey.question','conditional_option_id', string="Conditionals Questions")