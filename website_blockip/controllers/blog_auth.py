# -*- coding: utf-8 -*-

from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.addons.website_blog.controllers.main import WebsiteBlog
from openerp.addons.website_blog.controllers.main import QueryURL


class WebsiteBlog(WebsiteBlog):
    @http.route([
        '/blog',
        '/blog/page/<int:page>',
    ], type='http', auth="loged_in_or_ip", website=True)
    def blogs(self, page=1, **post):
        res = super(WebsiteBlog, self).blogs(page, post)
        return res

    @http.route([
        '/blog/<model("blog.blog"):blog>',
        '/blog/<model("blog.blog"):blog>/page/<int:page>',
        '/blog/<model("blog.blog"):blog>/tag/<model("blog.tag"):tag>',
        '/blog/<model("blog.blog"):blog>/tag/<model("blog.tag"):tag>/page/<int:page>',
    ], type='http', auth="loged_in_or_ip", website=True)
    def blog(self, *a, **kw):
        res = super(WebsiteBlog, self).blog(*a, **kw)
        return res

    @http.route([
        '''/blog/<model("blog.blog"):blog>/post/<model("blog.post", "[('blog_id','=',blog[0])]"):blog_post>''',
    ], type='http', auth="loged_in_or_ip", website=True)
    def blog_post(self, *a, **kw):
        return super(WebsiteBlog, self).blog_post(*a, **kw)

