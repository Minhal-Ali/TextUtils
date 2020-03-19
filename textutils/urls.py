from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about,name="index"),
    path('removepunc/', views.removepunc,name="removepunc"),
    path('capitalizefirst/', views.capitalizefirst,name="capitalizefirst"),
    path('newlineremove/', views.newlineremove,name="newlineremove"),
    path('spaceremover/', views.spaceremover,name="spaceremover"),
    path('charcounter/', views.charcounter,name="charcounter"),
]
