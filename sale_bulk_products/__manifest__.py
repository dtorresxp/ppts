# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Bulk products',
    'version': '10.0.2.0.0',
    'category': 'Sale',
    'depends': ['base', 'sale','product','stock'],
    'author': 'PPTS [India] Pvt.Ltd.',
    'summary': 'Multiple Products in line item',
    'description': 'Used to select bulk products to confirm sale.',
    'website': 'https://www.pptssolutions.com',
    'data': [
        'views/sale_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
