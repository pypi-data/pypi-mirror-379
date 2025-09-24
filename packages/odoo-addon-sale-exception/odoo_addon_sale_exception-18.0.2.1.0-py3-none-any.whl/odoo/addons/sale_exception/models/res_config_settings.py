# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sale_exception_show_popup = fields.Boolean(
        related="company_id.sale_exception_show_popup",
        readonly=False,
    )
