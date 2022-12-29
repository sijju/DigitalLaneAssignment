from django.urls import path,include
from . import views


urlpatterns = [
  path('votes',views.likes,name='likes'),
  path('vote/<str:pk>',views.updateLike)
    
]