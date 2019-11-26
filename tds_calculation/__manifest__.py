{
    'name': 'TDS Calculation',
    'version': '0.10',
    'category': 'TDS',
    'summary': 'TDS Functionality',
    'author': 'Prixgen Tech Solutions Pvt Ltd.',
    'company': 'Prixgen Tech Solutions Pvt Ltd.',
    'website': 'https://www.prixgen.com',
    'depends': ['base','stock','product','purchase','account','account_asset','prix_analytic_account'],
    'data': [
        'views/tds_group_settings_view.xml',
        'views/tds_mapping.xml',
        'views/tds_group.xml',
        'views/tds_section.xml',
        'views/assesse_code.xml',
        'views/concession_code.xml',
        'views/tds_nod.xml',
        'views/nod_configuration.xml',
        'views/round_off_view.xml',
        'views/account_invoice.xml',

        'views/res_partner.xml',
        'views/purchase.xml',
        'views/res_config_settings_views.xml',
        'security/groups.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False,
}