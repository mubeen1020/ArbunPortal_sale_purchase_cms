# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSalesMenu(http.Controller):
#     @http.route('/custom_sales_menu/custom_sales_menu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sales_menu/custom_sales_menu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sales_menu.listing', {
#             'root': '/custom_sales_menu/custom_sales_menu',
#             'objects': http.request.env['custom_sales_menu.custom_sales_menu'].search([]),
#         })

#     @http.route('/custom_sales_menu/custom_sales_menu/objects/<model("custom_sales_menu.custom_sales_menu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sales_menu.object', {
#             'object': obj
#         })

