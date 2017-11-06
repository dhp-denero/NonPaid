{
    'name': "Vuente Website Membership Signup",
    'version': "10.0",
    'author': "Vuente",
    'category': "Tools",
    'summary': "Creates signup forms for membeships",
    'description': "Creates signup forms for membeships",
    'license':'LGPL-3',
    'data': [
        'views/product_template_views.xml',
        'views/vuente_website_membership_signup_templates.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images':[
        'static/description/1.jpg',
    ],
    'depends': ['website', 'membership','website_sale'],
    'installable': True,
}