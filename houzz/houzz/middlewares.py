class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # change on proxy which you need
        request.meta['proxy'] = "https://35.162.160.108:8080"
