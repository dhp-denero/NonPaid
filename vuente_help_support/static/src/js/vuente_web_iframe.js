openerp.vuente_help_support = function (session) {


    var _t = session.web._t,
       _lt = session.web._lt;

    var vuente_help_support = session.vuente_help_support;

    session.web.client_actions.add('vuente_help_support.iframe', 'session.vuente_help_support.iframe');
    vuente_help_support.iframe = session.web.Widget.extend({
        template: 'vuente_help_support.iframe',

        /**
         * @param {Object} parent parent
         * @param {Object} [options]
         * @param {Array} [options.domain] domain on the Wall
         * @param {Object} [options.context] context, is an object. It should
         *      contain default_model, default_res_id, to give it to the threads.
         */
        init: function (parent, action) {
            this._super(parent, action);
            this.action = _.clone(action);
            this.action.params = _.extend({
                'link': 'https://yelizariev.github.io/',
            }, this.action.params);
        },
        start: function() {
            this.$el.find('iframe').css({height: '100%', width: '100%', border: 0});
            this.$el.find('iframe').attr({src: this.action.params.link});
            this.$el.find('iframe').on("load", this.bind_events.bind(this));
            return this._super();
        },
        bind_events: function(){
            //this.$el.find('iframe').contents().click(this.iframe_clicked.bind(this));
        },
        iframe_clicked: function(e){
        }
    })
}