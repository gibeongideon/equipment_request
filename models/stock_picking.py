
from odoo import fields, models


class StockPicking(models.Model):
    """
    Model representing internal transfers related to equipment requests.
    This model inherits from the `stock.picking` model and adds a Many2one field
    `equipment_transfer_id` to link internal transfers with equipment requests.
    This field is used to associate internal transfers with the corresponding
    equipment request.
    """
    _inherit = 'stock.picking'

    equipment_transfer_id = fields.Many2one('equipment.request',
                                            string='Equipment')
