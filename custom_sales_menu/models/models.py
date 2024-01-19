from odoo import models, fields, api

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    booking_datetime = fields.Datetime('Date and Time of Booking')
    mode_of_payment = fields.Many2one('payment.method',string='Modes of Payment')


