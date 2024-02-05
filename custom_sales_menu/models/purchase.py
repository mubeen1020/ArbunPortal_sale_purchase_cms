from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        related_so = self.env['sale.order'].search([('name', '=', self.origin)])
        if related_so:
            related_so.create_account_button()

        return res
