from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('who', views.who, name='who'),
    # path('services', views.services, name='services'),
    path('ongoing', views.ongoing, name='ongoing'),
    path('clients', views.clients, name='clients'),
    path('contact', views.contact, name='contact'),
    # path('more', views.more, name='more'),
    path('about', views.about, name='about'),
    path('clients', views.clients, name='clients'),
    path('Digital_Marketing', views.Digital_Marketing, name='Digital_Marketing'),
    path('full_stack', views.full_stack, name='full_stack'),
    path('Recruitments', views.Recruitments, name='Recruitments'),
    path('software_deve', views.software_deve, name='software_deve'),
    path('tap', views.tap, name='tap'),
    path('training', views.training, name='training'),
]
