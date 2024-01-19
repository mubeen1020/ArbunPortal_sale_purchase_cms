from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    booking_datetime = fields.Datetime(string='Booking Datetime')
    customer_name = fields.Char(string='Customer Name')
    mode_of_payment = fields.Char(string='Mode of Payment')