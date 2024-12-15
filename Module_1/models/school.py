from odoo import api, models, fields

class SchoolProfile(models.Model):
    _name = 'school.profile'
    _description = 'School Profile'

    name = fields.Char(string='School Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    virtual_class_support = fields.Boolean(string='Virtual Class Support?')
    school_rank = fields.Integer(string='School Rank')
    result = fields.Float(string='Result')
    address = fields.Text(string='School Address')
    establish_date = fields.Date(string='Establish Date')
    open_datetime = fields.Datetime(string='Open Date')
    school_type = fields.Selection([
        ('public','Public School'),
        ('private','Private School')
    ], string='School Type')
    documents = fields.Binary(string='Upload File')
    file_name = fields.Char(string='File Name')
    school_image = fields.Image(string='School Image')
    school_description = fields.Html(string='School Description')