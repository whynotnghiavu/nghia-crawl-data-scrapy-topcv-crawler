from scrapy.downloadermiddlewares.httpcache import HttpCacheMiddleware


class CustomHttpCacheMiddleware(HttpCacheMiddleware):
    def process_request(self, request, spider):
        if not self.should_cache_request(request):
            return None
        return super().process_request(request, spider)

    def should_cache_request(self, request):
        if '.html' in request.url:
            return True
        elif 'https://www.topcv.vn/tim-viec-lam-moi-nhat' in request.url:
            return False
        return False
