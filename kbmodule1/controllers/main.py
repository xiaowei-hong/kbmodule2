# -*- coding: utf-8 -*-
################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
################################################################################

from odoo import http
from odoo.http import request


class kbmodule1(http.Controller):

    @http.route(["/productsinfo/k801.htm"], type='http', auth="public", website=True)
    def go_away(self):
		return http.local_redirect('http://www.premiumquartz.com/?p=1801')
	@http.route(["/productsinfo/k802.htm"], type='http', auth="public", website=True)
    def go_away(self):
		return http.local_redirect('http://www.premiumquartz.com/?p=1802')