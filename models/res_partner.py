from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_recurring_business = fields.Boolean(
        string="Is Recurring Business",
        compute="_compute_is_recurring_business",
        search="_search_is_recurring_business"
    )

    @api.depends('create_date')
    def _compute_is_recurring_business(self):
        one_year_ago = fields.Datetime.now() - relativedelta(years=1)
        for partner in self:
            if partner.create_date and partner.create_date < one_year_ago:
                partner.is_recurring_business = True
            else:
                partner.is_recurring_business = False

    def _search_is_recurring_business(self, operator, value):
        one_year_ago = fields.Datetime.now() - relativedelta(years=1)
        if (operator == '=' and value) or (operator == '!=' and not value):
            return [('create_date', '<', one_year_ago)]
        else:
            return [('create_date', '>=', one_year_ago)]
