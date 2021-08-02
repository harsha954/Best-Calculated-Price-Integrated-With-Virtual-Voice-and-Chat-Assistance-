
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from PricePredictor.views import find

from PricePredictor.views import login, registration, logout

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='loginaction'),

    path('registration/',TemplateView.as_view(template_name = 'registration.html'),name='registration'),
    path('regaction/',registration,name='regaction'),

    path('find/',find, name='find'),

    path('logout/',logout,name='logout'),
]
