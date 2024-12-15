from odoo import api,fields,models

class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'School Course'

    title = fields.Char(string='Course Title')
    course_code = fields.Char(string='Course Code')
    description = fields.Text(string='Description')