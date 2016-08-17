# -*- coding: utf-8 -*-

{
    'name': 'Web Menu',
    'version': '1.0',
    'author': 'Rushi Patel',
    'description': 'Toggle Left Side Menu Bar',
    'category': 'Web',
    'depends': ['web'],
    'data': [
        'views/templates.xml',
    ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'application': True,
    'auto_install': False,
}
