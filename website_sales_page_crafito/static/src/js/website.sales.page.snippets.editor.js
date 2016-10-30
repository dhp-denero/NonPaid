odoo.define('website_sales_pages.editor', function (require) {
'use strict';

var Model = require('web.Model');
var ajax = require('web.ajax');
var core = require('web.core');
var base = require('web_editor.base');
var web_editor = require('web_editor.editor');
var options = require('web_editor.snippets.options');
var snippet_editor = require('web_editor.snippet.editor');
var session = require('web.session');
var website = require('website.website');
var _t = core._t;
var Widget = require('web.Widget');
var contentMenu = require('website.contentMenu');

options.registry.buy_now_button = options.Class.extend({
    drop_and_build_snippet: function() {
        var self = this;
        var model = new Model('product.product');
	    model.call('name_search', [], { context: base.get_context() }).then(function (product_ids) {

	        website.prompt({
			    id: "editor_new_buy_now",
			    window_title: _t("Select a Product"),
			    select: "Select a Product",
			    init: function (field) {
			        return product_ids;
			    },
			}).then(function (product_id) {
				self.$target.html("<div class=\"col-md-12 text-center mt16 mb32\">\n<h2><a class=\"btn btn-warning btn-lg\" href=\"/buy/now?product_id=" + product_id + "\">Buy Now</a></h2>\n</div>");
			});

        });
    },

});

});