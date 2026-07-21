# -*- coding: utf-8 -*-
{
    'name': 'Simple Library',
    'summary': 'Basit kütüphane kitap yönetimi',
    'version': '17.0.1.0.0',
    'author': 'Sude Atansay',
    'license': 'LGPL-3',
    'category': 'Library',
    'depends': ['base','mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}