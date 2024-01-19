# __manifest__.py
{
    'name': 'Custom Sales Menu',
    'version': '1.0',
    'summary': 'Changes Sales menu to Booking',
    'sequence': 10,
    'description': "Change Sales menu to Booking",
    'category': 'Custom',
    'author': 'Your Name',
    'website': 'https://www.yourcompany.com',
    'depends': ['sale'],
    'data': [
        'views/sales_menu_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
