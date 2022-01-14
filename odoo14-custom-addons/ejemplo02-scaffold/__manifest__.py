# -*- coding: utf-8 -*-
{
    'name': "Ejemplo02-scaffold",

    'summary': """
        Ejemplo02 Editado este esta editado el Ejemplo02 editado.""",

    'description': """
        Ejemplo02 Editado este esta editado el EJmplo02 editado.
    """,

    'author': "Marcosmartin16",
    'website': "https://github.com/Marcosmartin16",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
