from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_employee, name='view_employee'),
    path('add/' , views.add, name='add'),
] 