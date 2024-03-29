{
    "name": "Document management",
    "version": "13.0.1.0.0",
    "author": "V. Budvytis",
    "category": "Extra Tools",
    'summary': 'Store information about various documents or books',
    'description': 'A module to manage documents or books with: name, description and company information.',
    'depends': ['base'],
    'data': [
        'views/document_views.xml',
        'views/document_action.xml',
        'views/document_wizard.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}