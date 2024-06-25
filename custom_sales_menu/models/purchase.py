from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        self.create_account_entry_for_confirmed_po()
        return res

    def create_account_entry_for_confirmed_po(self):
        for po in self:
            related_so = self.env['sale.order'].search([('name', '=', po.origin)], limit=1)
            if not related_so:
                return
            
            vendor_name = po.partner_id.name
            vendor_id = po.partner_id.id
            purchase_order_name = po.name
            total_purchase_order_amount = po.amount_total

            balance = related_so.amount_total - total_purchase_order_amount
            customer_due = related_so.amount_total - total_purchase_order_amount if related_so.mode_of_payment.name == 'Cash' else 0.00
            vendor_due = total_purchase_order_amount - related_so.amount_total if related_so.mode_of_payment.name != 'Cash' else 0.00
            vendor_due = total_purchase_order_amount  if related_so.mode_of_payment.name == 'Bank' or related_so.mode_of_payment.name == 'Card' else 0.00

            account_vals = {
                'vendor_name': vendor_name,
                'vendor_id' : vendor_id,
                'quotation_date': related_so.date_order,
                'sale_order_name': related_so.name,
                'purchase_order_name': purchase_order_name, 
                'customer_due': customer_due,
                'vendor_due': vendor_due,
                'status': related_so.mode_of_payment.name,
            }
            
            self.env['custom.accounting'].create(account_vals)
