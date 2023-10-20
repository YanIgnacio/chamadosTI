from . import views
from django.urls import path

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('login/',views.loginView, name='login'),
    path('cadastro/',views.cadastroView, name='cadastro'),
    path('sairFunc/', views.sairFunc, name='sairFunc'),
    path('chamado/<int:idChamado>',views.chamado, name='chamado'),
    path('abrirChamado', views.abrirChamado, name='abrirChamado'),
    path('indicadores', views.indicadores, name='indicadores'),
    path('editaChamado/<int:idChamado>', views.editaChamado, name='editaChamado')
]
