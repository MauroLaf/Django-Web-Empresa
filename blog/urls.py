from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
   path('', views.blog, name="blog"),
   path('category/<int:category_id>',views.category, name="category"),#<category_id> este parametro dinamico siempre se detecta como "string" asi que si es un id debe ser un int y debemos forzarlo a cambiar
]
