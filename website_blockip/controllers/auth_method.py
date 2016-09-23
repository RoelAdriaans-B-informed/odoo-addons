# -*- coding: utf-8 -*-

import logging
_logger = logging.getLogger(__name__)

import openerp
from openerp import exceptions, http, models
from openerp.http import request

try:
    from netaddr import IPNetwork, IPAddress
except ImportError:
    _logger.debug('Cannot `import netaddr`.')


class IrHttp(models.Model):
    _inherit = 'ir.http'

    def _get_ipaddress(self):
        if 'HTTP_X_FORWARD_FOR' in request.httprequest.environ:
            _logger.info("From forward_for: {}".format(request.httprequest.environ['HTTP_X_FORWARD_FOR']))
            return request.httprequest.environ['HTTP_X_FORWARD_FOR']
        else:
            _logger.info("From remote_addr: {}".format(request.httprequest.environ['REMOTE_ADDR']))
            return request.httprequest.environ['REMOTE_ADDR']

    def _auth_method_loged_in_or_ip(self):
        ipadress = IPAddress(self._get_ipaddress())
        ip_good = False
        # self.pool['website.internal_ip'].get_object_reference(request.cr, openerp.SUPERUSER_ID, 'base','public_user')
        ip_ids = self.pool['website.internal_ip'].search(request.cr, openerp.SUPERUSER_ID, [])
        ips = self.pool['website.internal_ip'].read(request.cr, 1, ip_ids)
        for network in ips:
            if ipadress in IPNetwork(network['name']):
                ip_good = True
                continue

        if ip_good:
            self._auth_method_public()
        else:
            _logger.info("IP Address blocked, needs to login: {}".format(ipadress))
            self._auth_method_user()
