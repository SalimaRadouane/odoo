# -*- coding: utf-8 -*-
{
    'name': "Formation",

    'summary': 'Formation Management software',

    'sequence': -100,

    'description': """Formation Management software""",

    'author': "Aya Salima",
    

    
    'category': 'Project Management',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'mail', 'board'],

    'data': [
        'security/ir.model.access.csv',
        'views/session_views.xml',
        'views/formateur_views.xml',
        'views/theme_views.xml',
        'views/participant_views.xml',
        'views/templates.xml',
        'reports/session_details_template.xml',
        'reports/report.xml',
        'data/mail_templates.xml',
        'views/dashboard.xml',

    ],

    "qweb": [
        'static/src/xml/qweb_template.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}