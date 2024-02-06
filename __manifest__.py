{
    "name": "Document managment tool",
    "version": "13.0.1.0.0",
    "sequence": 30,
    "author": "V. Budvytis",
    "category": "Extra Tools",
    'summary': 'Store information about various documents or books',
    'description': 'A module to manage documents or books with: name, description and company information.',
    'depends': ['base'],
    'data': [
        'views/library_document_views.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
    ],
    'installable': True,
    'application': True,
}
