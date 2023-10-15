from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('giris/',views.giris, name="giris"),
    path('kayit/',views.kayit, name="kayit"),
    path('profil/',views.profil, name="profil"),
    path('<int:iha_id>/', views.detail, name="detail"),
    path('kiraliste/', views.kiraliste, name='kiraliste'),
    path('kirala/<int:iha_id>/', views.kirala, name='kirala'),

]
