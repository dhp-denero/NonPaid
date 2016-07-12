{
    'name': "Vuente Automated Task Tunnel",
    'version': "1.1.4",
    'author': "Vuente",
    'category': "Tools",
    'summary': "Automaticly crate tasks during mail campaigns",
    'license':'LGPL-3',
    'data': [
        'views/marketing_campaign_activity.xml',
        'views/project_task_views.xml',
        'views/hr_department_views.xml',
        'views/hr_employee_views.xml',
        'views/marketing_campaign.xml',
        'views/mail_template_views.xml',
        'views/marketing_campaign_test_member_views.xml',
        'views/marketing_campaign_workitem.xml',
    ],
    'demo': [],
    'depends': ['project', 'hr', 'marketing_campaign'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}