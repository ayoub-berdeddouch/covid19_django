from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/',views.data, name='data'),
    path('news/', views.getNews,name='news'),
    path('country_data/', views.getCountryData, name='country_data'),
    path('top10/', views.topConfirm, name="top10"),
    path('globals/',views.globals, name="globals") # added recently
]
