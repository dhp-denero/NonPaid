odoo.define('vuente_web_kit.summernote_fontfamily', function (require) {
'use strict';

var core = require('web.core');
var summerEditor = require('web_editor.rte');
//require('summernote/summernote'); // wait that summernote is loaded
var _t = core._t;

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
