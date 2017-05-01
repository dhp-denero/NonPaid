# -*- coding: utf-8 -*-
{
    'name': "Quickbooks Online Sync",
    'version': "1.0",
    'author': "Vuente",
    'category': "Tools",
    'summary': "Syncs data with Quickbooks online",
    'description': "Syncs data with Quickbooks online",
    'license':'LGPL-3',
    'data': [
        'views/migration_quickbooks_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'depends': ['account','hr'],
    'external_dependencies': {'python': ['requests_oauthlib']},
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
    'price': 1.00,
    'currency': 'EUR',
}