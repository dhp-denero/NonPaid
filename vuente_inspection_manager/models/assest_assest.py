# -*- coding: utf-8 -*-
from openerp import api, fields, models

class VuenteAssetAsset(models.Model):

    _inherit = "asset.asset"
        
    specification_ids = fields.One2many('vuente.specification', 'asset_id', string="Specifications")
    inspection_ids = fields.One2many('vuente.inspection', 'asset_id', string="Inspection")

    
class VuenteSpecification(models.Model):

    _name = "vuente.specification"
        
    asset_id = fields.Many2one('asset.asset', string="Asset")
    name = fields.Char(string="Name")
    
class VuenteInspection(models.Model):

    _name = "vuente.inspection"
        
    asset_id = fields.Many2one('asset.asset', string="Asset")
    name = fields.Char(string="Name")