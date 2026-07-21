from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'name, id'

    name = fields.Char(string='Kitap Adı', required=True)
    author = fields.Char(string='Yazar')
    category = fields.Selection(
        selection=[
            ('roman', 'Roman'),
            ('bilim', 'Bilim'),
            ('tarih', 'Tarih'),
            ('diger', 'Diğer'),
        ],
        string='Kategori',
    )
    is_available = fields.Boolean(string='Müsait', default=True)
    description = fields.Text(string='Açıklama')
    publication_date = fields.Date(string='Yayın Tarihi')
    pages = fields.Integer(string='Sayfa Sayısı')
    