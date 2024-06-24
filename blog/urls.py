from django.urls import path
from .views import *
urlpatterns =[
    path('',index,name='index'),
    path('detel/<int:id>/',index_detel, name="detel"),
    path('about/', about, name="about"),
    path('h404/',h404, name="h404"),
    path('contact/', contact, name="contact"),
    path('price/', price, name="price"),
    path('feature/', feature, name="feature"),
    path('quote/', quote, name="quote"),
    path('service/', service, name="service"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('detel2/<int:id>/',index_detel2, name="detel2"),
    path('detel3/<int:id>/',index_detel3, name="detel3"),
]
