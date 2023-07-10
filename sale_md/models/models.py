
from odoo import models, fields, api


class SaleOrderLineInherit(models.Model):
    _inherit='sale.order.line'


    @api.onchange('product_id')
    def _onchange_order_line(self):
        # select products in orders
        selected_products=[]
        # get parent sale order lines
        for line in self.order_id.order_line:
            selected_products .append(int(line.product_id))

        domain=[('id','not in',selected_products)]


        return {'domain': {'product_id': domain}}


