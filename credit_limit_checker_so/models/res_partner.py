from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    OVERCREDIT_ACTIONS = [('nothing','Do Nothing'),('warn','Warn'),('on_hold','Put On Hold')]

    is_over_credit = fields.Boolean('Over Credit',compute="_compute_over_credit",store=True)
    over_credit_action = fields.Selection(OVERCREDIT_ACTIONS,string="Action when credit limit is exceeded")
    
    @api.depends('credit','credit_limit')
    def _compute_over_credit(self):
        for rec in self:
            if rec.credit > rec.credit_limit:
                rec.is_over_credit = True
            else:
                rec.is_over_credit = False