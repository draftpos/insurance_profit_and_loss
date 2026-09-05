from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    is_recurring_business = fields.Boolean(
        string="Is Recurring Business",
        compute="_compute_is_recurring_business",
        store=True,
    )

    @api.depends('date', 'partner_id.create_date')
    def _compute_is_recurring_business(self):
        for line in self:
            if line.partner_id and line.partner_id.create_date and line.date:
                # If partner was created more than 1 year before this invoice/line date
                partner_create_date = line.partner_id.create_date.date()
                if line.date >= partner_create_date + relativedelta(years=1):
                    line.is_recurring_business = True
                else:
                    line.is_recurring_business = False
            else:
                line.is_recurring_business = False
