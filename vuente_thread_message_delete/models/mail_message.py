# -*- coding: utf-8 -*
import logging
_logger = logging.getLogger(__name__)
import io
import zipfile
import tempfile
import urllib
import os

from openerp import api, fields, models

class MailMessageDelete(models.Model):

    _inherit = "mail.message"

    @api.model
    def sw_delete_message(self,message_id):
        my_message = self.env['mail.message'].browse(message_id)
        my_message.unlink()