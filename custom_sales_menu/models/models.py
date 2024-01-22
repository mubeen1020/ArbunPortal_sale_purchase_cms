from odoo import models, fields, api
from datetime import timedelta

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    booking_datetime = fields.Datetime('Date and Time of Booking')
    adjusted_booking_time = fields.Char(compute='_compute_adjusted_booking_time')
    mode_of_payment = fields.Many2one('payment.method', string='Mode of Payment')

    @api.depends('booking_datetime')
    def _compute_adjusted_booking_time(self):
        for record in self:
            if record.booking_datetime:
                adjusted_time = record.booking_datetime + timedelta(hours=5)
                record.adjusted_booking_time = adjusted_time.strftime('%H:%M:%S')
            else:
                record.adjusted_booking_time = False
