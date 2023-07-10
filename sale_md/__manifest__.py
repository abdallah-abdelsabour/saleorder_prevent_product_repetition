# -*- coding: utf-8 -*-
{
    'name': "sale_md",

    'summary': """
       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "abdallah Abdelsabour",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
