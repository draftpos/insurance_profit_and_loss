from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    enable_insurance_pnl_format = fields.Boolean(
        string="Enable Insurance Profit and Loss Format",
        default=False,
        help="Use the custom Insurance layout for the Profit and Loss report."
    )
