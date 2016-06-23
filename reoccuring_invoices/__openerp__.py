{
    'name': "Reoccuring Invoices",
    'version': "1.0",
    'author': "Vuente",
    'category': "Tools",
    'summary':"Let's you send a partner an invoice every week/month",
    'data': [
        'views/account_invoice_reoccuring_views.xml',
        'data/ir.cron.csv',
    ],
    'demo': [],
    'images':[
        'static/description/1.jpg',
    ],
    'depends': ['account'],
    'installable': True,
}