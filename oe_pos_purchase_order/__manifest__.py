# -*- coding: utf-8 -*-
{
    'name': 'POS Purchase Order | Create Purchase Orders from POS | POS Procurement',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Create Purchase Orders directly from POS with one click - Quick POS Procurement Button',
    'description': """
POS Purchase Order for Odoo 18
==============================

Create Purchase Orders directly from your Point of Sale interface with a single click.

KEY FEATURES
============

QUICK ACCESS BUTTON
-------------------
- Adds a Purchase Order button to POS control buttons
- One-click access to purchase order creation
- Opens purchase order form in a new tab
- No interruption to POS workflow

SEAMLESS INTEGRATION
--------------------
- Works with Odoo 18 POS interface
- Integrates with existing POS control buttons
- Compatible with Community and Enterprise editions
- No complex configuration needed

PERFECT FOR
-----------
- Retail businesses needing on-the-fly stock reordering
- POS operators initiating vendor orders
- Businesses wanting quick procurement access from POS stations

MULTI-LANGUAGE SUPPORT
----------------------
- English, French, Spanish, German, Chinese, Arabic
- RTL support for Arabic

If you like this module, please rate us on Odoo App Store!
    """,
    'author': 'Sheikh Muhammad Saad, OdooElevate',
    'website': 'https://odooelevate.odoo.com/',
    'support': 'info.odooelevate@gmail.com',
    'license': 'LGPL-3',
    'currency': 'USD',
    'depends': ['point_of_sale', 'purchase'],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            '/oe_pos_purchase_order/static/src/js/purchase_order_button.js',
            '/oe_pos_purchase_order/static/src/xml/purchase_order_button.xml',
        ],
    },
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'sequence': 1,
}
