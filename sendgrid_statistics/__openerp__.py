{
    'name': "SendGrid Mail Statistics",
    'version': "1.0",
    'author': "Vuente",
    'category': "Tools",
    'website':'http://vuente.com/',
    'summary':'Gather statistics on all mail sent out via sendgrid',
    'description':'Gather statistics on all mail sent out via sendgrid',    
    'license':'LGPL-3',
    'data': [
        'views/mail_mail_sendgrid_statistic_views.xml',
        'views/mail_mail_sendgrid_account_views.xml',
        'data/ir.cron.csv',
    ],
    'demo': [],
    'depends': ['mail'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}