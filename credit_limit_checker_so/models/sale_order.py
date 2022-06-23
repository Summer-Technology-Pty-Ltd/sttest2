from odoo import models, api
from odoo.exceptions import ValidationError, Warning


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id:
            if self.partner_id.is_over_credit:
                if self.partner_id.over_credit_action == 'nothing':
                    pass
                elif self.partner_id.over_credit_action == 'warn':
                    raise Warning("Warning! this customer exceeded his credit limit")
                elif self.partner_id.over_credit_action == 'on_hold':
                    raise ValidationError('This customer exceeded his credit limit and has been put on hold, please select a different customer')
        super(SaleOrder, self).onchange_partner_id()

    