from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('notes',views.notes, name="notes"),
    path('search',views.search, name="search"),
    path('feedback',views.feedback, name="feedback"),
    path('C',views.cpro, name="C"),
    path('',views., name=""),
    path('',views., name=""),
    path('',views., name=""),
    path('',views., name=""),

    ]
