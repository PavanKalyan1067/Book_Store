from accounts.models import Information


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'GET' or request.method == 'DELETE':
            url = request.path
            method = request.method
            Information.objects.create(method=method, url=url)

        return response
