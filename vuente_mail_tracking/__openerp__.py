{
    'name': "Vuente Mail Tracking",
    'version': "1.2",
    'author': "Vuente",
    'category': "Tools",
    'summary': "Tracks campaign mail open/reply/bounce rate",
    'license':'LGPL-3',
    'data': [
        'views/marketing_campaign_views.xml',
        'views/mail_template_views.xml',
    ],
    'demo': [],
    'depends': ['mass_mailing','marketing_campaign'],
    'images':[
        'static/description/1.jpg',
        'static/description/2.jpg',        
    ],
    'installable': True,
}