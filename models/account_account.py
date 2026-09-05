from odoo import models, fields

class AccountAccount(models.Model):
    _inherit = 'account.account'

    insurance_report_category = fields.Selection([
        ('managed_fund', 'Managed Fund (Revenue)'),
        ('management_fees_general', 'Management Fees - General Fund'),
        ('management_fees_managed', 'Management Fees - Managed Fund'),
        ('other_income', 'Other Income'),
        ('unrealised_profit', 'Unrealised Profit on Equities')
    ], string="Insurance Report Category", help="Used to map specific accounts to the custom Insurance Profit and Loss report.")
