# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, fields, models

class ProjectProjectTeam(models.Model):

    _inherit = "project.project"
    
    task_team_ids = fields.Many2many('res.partner', string="Team Members")
    vuente_tags = fields.Many2many('project.vuente.tags', string="Tags")
    
class ProjectProjectVuenteTags(models.Model):

    _name = "project.vuente.tags"
    
    name = fields.Char(string="Name")
    