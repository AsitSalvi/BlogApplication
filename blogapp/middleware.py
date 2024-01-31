from django.http import HttpResponseForbidden
from django.urls import reverse

class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = [reverse('login'), reverse('signup'), '/admin/']
        if request.path.startswith('/admin/') or request.path in excluded_paths:
            return self.get_response(request)
        
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You don't have access to this page.")
        
        return self.get_response(request)
