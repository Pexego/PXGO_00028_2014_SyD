# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Pexego All Rights Reserved
#    $Jesús Ventosinos Mayor <jesus@pexego.es>$
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

{
    'name': "Document customizations",
    'version': '2.0',
    'category': '',
    'description': """""",
    'author': 'Pexego',
    'website': '',
    "depends": ['report', 'sale', 'stock', 'sale_stock', 'picking_services',
                'delivery', 'supplier_ref', 'sale_layout', 'product_pack',
                'syd_custom', 'purchase_discount','stock_picking_invoice_link'],

    "data": ['views/sale_view.xml', 'views/payment_mode_view.xml', 'views/stock_view.xml',
             'qweb_report/ir_qweb.xml', 'qweb_report/report_proforma.xml',
             'qweb_report/report_saleorder.xml', 'qweb_report/report_stockpicking.xml',
             'qweb_report/valued_picking_report.xml', 'qweb_report/report_purchase_order.xml',
             'qweb_report/report_header.xml', 'qweb_report/report_invoice.xml',
             'qweb_report/purchase_quotation.xml',
             'sale_report.xml', 'stock_report.xml', 'account_report.xml',
             'data/paperformat_data.xml'],
    "installable": True
}
