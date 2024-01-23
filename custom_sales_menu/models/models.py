from odoo import models, fields, api
from datetime import timedelta


import logging

_logger = logging.getLogger(__name__)

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

    vendor_names1 = fields.Char(
        string='Vendors', compute='_compute_vendor_names'
    )

    @api.depends('partner_id.name')
    def _compute_vendor_names(self):
        for record in self:
                vendors = set()
                related_pos = self.env['purchase.order'].search([('origin','=',record.name)])
                for po in related_pos:
                    vendors.add(po.partner_id.name)
                record.vendor_names1 = ", ".join(vendors)    

            
    display_name = fields.Char(compute='_compute_display_name')

    @api.depends('partner_id.name', 'vendor_names1')
    def _compute_display_name(self):
        for record in self:
            customer_name = record.partner_id.name if record.partner_id else ''
            vendors = record.vendor_names1 if record.vendor_names1 else 'No Vendors'
            record.display_name = f"{customer_name} ({vendors})"