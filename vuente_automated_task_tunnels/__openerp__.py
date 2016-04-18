{
    'name': "Vuente Automated Task Tunnel",
    'version': "1.0",
    'author': "Vuente",
    'category': "Tools",
    'summary': "Automaticly crate tasks during mail campaigns",
    'license':'LGPL-3',
    'data': [
        'views/marketing_campaign_activity.xml',
        'views/project_task_views.xml',
        'views/hr_department_views.xml',
        'views/hr_employee_views.xml',
    ],
    'demo': [],
    'depends': ['project', 'hr', 'marketing_campaign'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}