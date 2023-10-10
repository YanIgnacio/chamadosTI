from . import views
from django.urls import path

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('login/',views.loginView, name='login'),
    path('sairFunc/', views.sairFunc, name='sairFunc'),
    path('chamado/',views.chamado, name='chamado'),
]
