
from odoo import models, fields, api
from datetime import datetime


class CustomAccountingReportWizard(models.TransientModel):
    _name = 'custom.accounting.report.wizard'
    _description = 'Custom Accounting Report Wizard'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    vendor_id = fields.Many2one('res.partner', string='Vendor')

    def print_report(self):
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'vendor_id': self.vendor_id.id if self.vendor_id else None,
        }
        return self.env.ref('custom_sales_menu.custom_accounting_report').report_action(self, data=data)
    


class Reportballance(models.AbstractModel):

    _name = 'report.custom_sales_menu.custom_accounting_report_template2'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data is None:
            data = {}
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        vendor_id = data.get('vendor_id')
        print(vendor_id,"vendor_id")
        domain = []
        if start_date and end_date:
            domain += [
                ('quotation_date', '>=', start_date),
                ('quotation_date', '<=', end_date)
            ]
        if vendor_id:
            domain += [('vendor_id', 'in', [vendor_id])]

        records = self.env['custom.accounting'].search(domain)
        print(records)

        total_customer_due = sum(record.customer_due for record in records)
        total_vendor_due = sum(record.vendor_due for record in records)
        company_id = self.env.company
        # print(records[0].vendor_ids.name,"llllllllllllllllllllllllllllll")
        if company_id[0].logo:
            logo_base64 = company_id[0].logo.decode('utf-8')
        else:
            logo_base64 = None

        return {
            'doc_ids': docids,
            'doc_model': 'custom.accounting',
            'docs': records,
            'total_customer_due': total_customer_due,
            'total_vendor_due': total_vendor_due,
            'company': logo_base64,
        }