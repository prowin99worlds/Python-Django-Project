from django.urls import path
from django.views.generic.base import RedirectView
from .views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('pages/about-us.html', RedirectView.as_view(url='/about/')),
]
