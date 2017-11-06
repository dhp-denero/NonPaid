# -*- coding: utf-8 -*-
from openerp import api, fields, models
import logging
_logger = logging.getLogger(__name__)
import base64

class SurveyQuestionConditional(models.Model):

    _inherit = "survey.question"
    
    conditional = fields.Boolean(string="Conditional")
    conditional_question_id = fields.Many2one('survey.question', string="Condition Question", help="The question which determines if this question is shown")
    conditional_option_id = fields.Many2one('survey.label', string="Condition Option", help="The option which determines if this question is shown")
    type = fields.Selection( selection_add=[('binary', 'File Select')] )
    
    @api.multi
    def validate_binary(self, post, answer_tag):
        self.ensure_one()
        errors = {}
        
        # Empty answer to mandatory question
        if self.constr_mandatory and answer_tag not in post:
            errors.update({answer_tag: self.constr_error_msg})
            
        return errors
