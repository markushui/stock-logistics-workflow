# Copyright 2020 Tecnativa - Ernesto Tejeda
# Copyright 2023 Moduon Team - Eduardo de Miguel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock batch picking account",
    "summary": "Generates invoices when batch is set to Done state",
    "version": "16.0.1.0.3",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "maintainers": ["ernestotejeda"],
    "development_status": "Beta",
    "category": "Warehouse Management",
    "depends": ["stock_picking_batch", "sale"],
    "website": "https://github.com/OCA/stock-logistics-workflow",
    "data": ["views/stock_batch_picking.xml", "views/res_partner_views.xml"],
    "installable": True,
    "license": "AGPL-3",
}
