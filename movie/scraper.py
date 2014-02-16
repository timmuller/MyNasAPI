from django.views.generic import View
from django.http import HttpResponse


class Scraper(View):
    def get(self, request):
        return HttpResponse("ok");
