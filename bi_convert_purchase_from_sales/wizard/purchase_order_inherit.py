from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    booking_datetime = fields.Datetime('Date and Time of Booking')
    customer_name = fields.Char(string='Customer Name')
    mode_of_payment = fields.Char(string='Mode of Payment')
  