# -*- coding: utf-8 -*-
from openerp import api, fields, models
import logging
_logger = logging.getLogger(__name__)
import base64

class SurveyUserInputLineBinary(models.Model):

    _inherit = "survey.user_input_line"
    
    binary_data = fields.Binary(string="Binary Data")
    binary_data_filename = fields.Char(string="Binary Data Filename")
    answer_type = fields.Selection( selection_add=[('binary', 'File Select')] )
    
    @api.model
    def save_line_binary(self, user_input_id, question, post, answer_tag):
        vals = {
            'user_input_id': user_input_id,
            'question_id': question.id,
            'survey_id': question.survey_id.id,
            'skipped': False,
        }        
        if answer_tag in post:
            _logger.error("save binary")
            answer = base64.encodestring(post[answer_tag].read() )
            _logger.error(answer)
            _logger.error(post[answer_tag].filename)
            vals.update({'answer_type': 'binary', 'binary_data': answer, 'binary_data_filename': post[answer_tag].filename})
        else:
            vals.update({'answer_type': None, 'skipped': True})
        old_uil = self.search([
            ('user_input_id', '=', user_input_id),
            ('survey_id', '=', question.survey_id.id),
            ('question_id', '=', question.id)
        ])
        if old_uil:
            old_uil.write(vals)
        else:
            old_uil.create(vals)
        return True