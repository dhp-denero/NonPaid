import openerp.http as http
from openerp.http import request
import logging
_logger = logging.getLogger(__name__)
import werkzeug
import base64
import json
import openerp
import re

from openerp.addons.website.models.website import slug

class BuyNowController(http.Controller):

    @http.route('/buy/now', website=True, type='http', auth="public")
    def buy_now(self, **kw):

        values = {}
	for field_name, field_value in kw.items():
            values[field_name] = field_value
        
        product = request.env['product.product'].browse(int(values['product_id']) )

        order = request.website.sale_get_order(force_create=1)

        cart_values = order._cart_update(product_id=product.id, add_qty=1)

        return request.redirect("/shop/checkout")