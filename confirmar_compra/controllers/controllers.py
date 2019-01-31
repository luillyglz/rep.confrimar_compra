# -*- coding: utf-8 -*-
from odoo import http

# class ConfirmarCompra(http.Controller):
#     @http.route('/confirmar_compra/confirmar_compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/confirmar_compra/confirmar_compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('confirmar_compra.listing', {
#             'root': '/confirmar_compra/confirmar_compra',
#             'objects': http.request.env['confirmar_compra.confirmar_compra'].search([]),
#         })

#     @http.route('/confirmar_compra/confirmar_compra/objects/<model("confirmar_compra.confirmar_compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('confirmar_compra.object', {
#             'object': obj
#         })