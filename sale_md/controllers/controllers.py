# -*- coding: utf-8 -*-
# from odoo import http


# class SaleMd(http.Controller):
#     @http.route('/sale_md/sale_md', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_md/sale_md/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_md.listing', {
#             'root': '/sale_md/sale_md',
#             'objects': http.request.env['sale_md.sale_md'].search([]),
#         })

#     @http.route('/sale_md/sale_md/objects/<model("sale_md.sale_md"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_md.object', {
#             'object': obj
#         })
