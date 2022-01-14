# -*- coding: utf-8 -*-
{
    'name': "lista_tareas",

    'summary': """
        Sencilla lista de tareas""",

    'description': """
        Lista de tareas utilizada para crear un nuevo moudlo con un 
         nuevo modelo de datos
    """,

    'author': "Marcosmartin16",
    'website': "https://github.com/Marcosmartin16",

    'application': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
}

