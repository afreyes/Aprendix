from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('listarcurso/', views.listarcurso, name="listarcurso"),
    path('agregarcurso/', views.agregarcurso, name="agregarcurso"),
    path('actualizarcurso/<int:idcurso>/', views.actualizarcurso, name="actualizarcurso"), 
    path('eliminarcurso/<int:idcurso>/', views.eliminarcurso, name="eliminarcurso"),  
]