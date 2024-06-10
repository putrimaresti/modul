# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Modul pendataan pasien pada RS Sulianti Saroso""",

    'description': """
        Modul ini berfungsi untuk para karyawan mendata pasien yang berobat di RS Sulianti Saroso
    """,

    'author': "Putri Maresti",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/patient.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
