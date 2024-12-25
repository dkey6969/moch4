from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ITSpecialistMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            level = request.POST.get("level")
            if level not in ["jun", "middle", "senior"]:
                return HttpResponseBadRequest("Пожалуйста, подтяните ваш уровень, минимально допустимый уровень — jun.")

