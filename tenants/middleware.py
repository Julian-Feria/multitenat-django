from django.utils.deprecation import MiddlewareMixin

class DebugTenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"Host recibido: {request.get_host()}")