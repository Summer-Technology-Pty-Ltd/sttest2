# -*- coding: utf-8 -*-
{
    'name': "Credit Limit Checker",
    'summary': """
        Credit Limit checker in Sale Order""",
    'description': """
        Credit Limit checker in Sale Order
    """,
    'author': "Christopher Yang",
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'depends': [
                'base','sale',
    ],
    'data': [
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
