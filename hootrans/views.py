from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

class IndexView(TemplateView):
    template_name = "index.html"
    def post(self, request):
        if request.method == 'POST':
            return HttpResponseRedirect('/map')

class MapView(TemplateView):
    template_name = "map.html"