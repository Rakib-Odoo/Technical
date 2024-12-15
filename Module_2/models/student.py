from odoo import api, fields, models
from datetime import date

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Student Name')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender')
    image = fields.Binary(string='Image')
    age = fields.Integer(string='Age', compute='_compute_age')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
