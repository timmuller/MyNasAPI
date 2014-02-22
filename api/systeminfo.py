import json
import subprocess
from django.views.generic import View
from django.http import HttpResponse

class SystemInfo(View):
    def get(self, request):
        system_info = {}
        system_info['memory_total'] = self.get_memory_total()
        return HttpResponse(json.dumps(system_info), content_type='application/json');

    def get_memory_total(self):
        return "ok"