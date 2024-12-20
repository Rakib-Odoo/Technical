{
    'name': 'Student',
    'version': '1.1.3',
    'category': 'School Management',
    'summary': 'School management system supported in odoo13.',
    'description': 'School management system supported in odoo13.',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/view_menu.xml',
        'views/view_student.xml',
        'views/view_course.xml',
        'demo/student_demo_data.xml',
        'demo/course_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
