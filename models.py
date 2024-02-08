from odoo import models, fields, api

class CustomDocuments(models.Model):
    _name = 'doc.manager'
    _description = 'Documents Manager'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company')

class CustomDocumentWizard(models.TransientModel):
    _name = 'doc.manager.wizard'
    _description = 'Documents Manager Wizard'

    date_from = fields.Date(string='From Date', required=True)
    date_to = fields.Date(string='To Date', required=True)

    def print_documents(self):
        document_obj = self.env['doc.manager']

        documents = document_obj.search([
            ('create_date', '>=', self.date_from + ' 00:00:00'),
            ('create_date', '<=', self.date_to + ' 23:59:59'),
        ])

        for document in documents:
            document.name