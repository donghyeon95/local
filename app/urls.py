from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
            path('', views.index, name ='index'),
            path('viewer/', views.pdf_view, name ='pdf_view'),
]
