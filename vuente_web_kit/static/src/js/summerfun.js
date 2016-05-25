odoo.define('vuente_web_kit.summernote_fontfamily', function (require) {
'use strict';

var core = require('web.core');
var summerEditor = require('web_editor.rte');
var options = require('web_editor.snippets.options');
require('summernote/summernote'); // wait that summernote is loaded
var _t = core._t;
var qweb = core.qweb;
var ajax = require('web.ajax');

ajax.loadXML('/vuente_web_kit/static/src/xml/website_color_picker_modal5.xml', qweb);

options.Class.include({
	    start: function () {
			if ( $("#custombgcolour").length == 0) {
			    $("div[title='Transparent']").eq(0).before("<div class='note-color-reset'><a id='custombgcolour'>Custom Back Colour</a></div>");
			    $("div[title='Reset']").eq(0).before("<div class='note-color-reset'><a id='customfrcolour'>Custom Fore Colour</a></div>");
			    $("#custombgcolour").click(function() {
     		        var self = this;
		            this.template = 'website_color_picker.color_background_picker_modal';
		            self.$modal = $( qweb.render(this.template, {}) );
		            $('body').append(self.$modal);
                    $('#oe_pick_background_modal').modal('show');

                    self.$modal.find("#submit_background_color").on('click', function () {
						var backColor = self.$modal.find("#colorbgpick").val();
						$.summernote.pluginEvents.applyFont(null, null, null, null, backColor, null);

                        //self.$target.css("background-color",self.$modal.find("#colorpick").val() );
                        self.$modal.modal('hide');
                    });

			    });
			    $("#customfrcolour").click(function() {
     		        var self = this;
		            this.template = 'website_color_picker.color_picker_modal';
		            self.$modal = $( qweb.render(this.template, {}) );
		            $('body').append(self.$modal);
                    $('#oe_pick_color_modal').modal('show');

                    self.$modal.find("#submit_color").on('click', function () {
						var foreColor = self.$modal.find("#colorfrpick").val();
						$.summernote.pluginEvents.applyFont(null, null, null, foreColor, null, null);

                        self.$modal.modal('hide');
                    });

			    });
		    }
    },
});

summerEditor.Class.include({
    config: function ($editable) {
        return {
            'airMode' : true,
            'focus': false,
            'airPopover': [
                ['style', ['style']],
                ['font', ['bold', 'italic', 'underline', 'clear']],
                ['fontsize', ['fontsize']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['table', ['table']],
                ['fontname', ['fontname']],
                ['insert', ['link', 'picture']],
                ['history', ['undo', 'redo']],
            ],
            'styleWithSpan': false,
            'inlinemedia' : ['p'],
            'lang': "odoo",
            fontNames: [
			        'Arial', 'Arial Black', 'Comic Sans MS', 'Courier New',
			        'Helvetica Neue', 'Helvetica', 'Impact', 'Lucida Grande',
			        'Tahoma', 'Times New Roman', 'Verdana'
            ],
            'onChange': function (html, $editable) {
                $editable.trigger("content_changed");
            }
        };
    },
});



});
