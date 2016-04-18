odoo.define('website.feature.boxes', function (require) {
'use strict';

var Model = require('web.Model');
var base = require('web_editor.base');
var options = require('web_editor.snippets.options');
var session = require('web.session');
var website = require('website.website');
var ajax = require('web.ajax');
var core = require('web.core');
var qweb = core.qweb;

/*
options.registry.feature_boxes = options.Class.extend({
    colourbg: function(type) {
		if (type !== 'click') return;
		var self = this;
		this.template = 'website_color_picker.color_picker_modal';
		self.$modal = $( qweb.render(this.template, {}) );
		$('body').append(self.$modal);
        $('#oe_social_share_modal').modal('show');

        self.$modal.find("#sub_map").on('click', function () {
            self.$target.attr('style', "background-color: " + self.$modal.find("#colorpick").val() );
            self.$modal.modal('hide');
        });

    },
});
*/


});