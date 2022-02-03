from odoo import http
from odoo.http import request

class OpenAcademy(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World odoo"

    @http.route('/hello_user', auth="user")
    def hello_user(self, **kw):
        return "Hello %s" %(request.env.user.name)

    @http.route('/hello_template')
    def hello_template(self, **kw):
        return request.render('estate.hello_world')

    @http.route('/hello_template_user')
    def hello_template_user(self, **kw):
        courses = request.env['estate.property'].search([('state', '=', 'cancel')])
        print ("courses ::: ", courses)
        return request.render('estate.hello_user', { 'user': request.env.user, 'courses': courses })