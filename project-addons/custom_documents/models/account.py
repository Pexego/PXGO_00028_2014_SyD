# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Comunitea All Rights Reserved
#    $Jesús Ventosinos Mayor <jesus@comunitea.com>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, exceptions, _
import openerp.addons.decimal_precision as dp


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    price_unit_net = fields.Float(string='Unit Price',
                                  digits= dp.get_precision('Product Price'),
                                  compute='_get_price_unit_net')

    @api.one
    @api.depends('price_unit', 'discount')
    def _get_price_unit_net(self):
        self.price_unit_net = self.price_unit * (1 - (self.discount / 100))
