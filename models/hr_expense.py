
from odoo import fields, models


class HrExpense(models.Model):
    """
    Model representing expenses associated with equipment requests.
    This model inherits from the `hr.expense` model and adds a Many2one field
    `equipment_expense_id` to link expenses with equipment requests. This field
    is used to associate expenses with the corresponding equipment request.
    """
    _inherit = "hr.expense"

    equipment_expense_id = fields.Many2one('equipment.request',
                                           string='Equipment')
