from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'STATIC_URL': '/static/'})

class AboutView(TemplateView):
    template_name = 'about-us.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, 'about-us.html', {'STATIC_URL': '/static/'})
