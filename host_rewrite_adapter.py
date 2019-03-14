from urllib.parse import urlparse

from requests.adapters import HTTPAdapter


class HostRewriteAdapter(HTTPAdapter):
    """`requests` adapter that rewrites host of original request"""

    host_header = 'Host'

    def __init__(self, new_host, *args, **kwargs):
        """
        :param str new_host: a host to connect
        """
        super(HostRewriteAdapter, self).__init__(*args, **kwargs)
        self.new_host = new_host

    def cert_verify(self, conn, url, verify, cert):
        """Disable cert verification because it fails when host is rewritten"""
        pass

    def add_headers(self, request, **kwargs):
        """Set 'Host' header to request"""
        super(HostRewriteAdapter, self).add_headers(request, **kwargs)
        request.headers[self.host_header] = urlparse(request.url).netloc

    def build_response(self, req, resp):
        """Remove 'Host' header from request because it interferes with cookies set to redirected resources"""
        req.headers.pop(self.host_header, None)
        return super(HostRewriteAdapter, self).build_response(req, resp)

    def get_connection(self, url, proxies=None):
        """Establishing connection to new host instead of original"""
        url = urlparse(url)
        # noinspection PyProtectedMember
        url = url._replace(netloc=self.new_host).geturl()
        return super(HostRewriteAdapter, self).get_connection(url, proxies)
