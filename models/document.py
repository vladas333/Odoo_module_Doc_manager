from odoo import models, fields, api

class Document(models.Model):
    _name = 'document.management'
    _description = 'Document Management'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    company_id = fields.Many2one('res.company', string='Company', required=True)