from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_insurance_pnl_format = fields.Boolean(
        string="Enable Insurance Profit and Loss Format",
        related="company_id.enable_insurance_pnl_format",
        readonly=False,
        help="Use the custom Insurance layout for the Profit and Loss report."
    )
