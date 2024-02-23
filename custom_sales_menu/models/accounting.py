from odoo import models, fields,api

class CustomAccounting(models.Model):
    _name = 'custom.accounting'
    _description = 'Custom Accounting'

    quotation_date = fields.Datetime(string='Quotation Date')
    purchase_order_name = fields.Char('Purchase Order',required=True)
    sale_order_name = fields.Char('Sale Order',required=True)
    vendor_name = fields.Char('Vendor Name',required=True)
    vendor_id = fields.Many2one('res.partner', string='Vendor')
    customer_due = fields.Float(string='Urban Due')
    vendor_due = fields.Float(string='Vendor Due')
    status = fields.Char(string='Status')

    @api.model
    def action_open_report_wizard(self, x=None):
        view_id = self.env.ref('custom_sales_menu.view_custom_accounting_report_wizard_form').id
        return {
            'name': 'Generate Report',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'custom.accounting.report.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': self.env.context,
        }
