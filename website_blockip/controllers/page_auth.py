# -*- coding: utf-8 -*-

from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.addons.website.controllers.main import Website


class Website(Website):
    @http.route('/page/<page:page>', type='http', auth="loged_in_or_ip", website=True)
    def page(self, *a, **kw):
        return super(Website, self).page(*a, **kw)
