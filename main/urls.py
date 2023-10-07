from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('notes',views.notes, name="notes"),
    path('about',views.about, name="about"),
    path('search',views.search, name="search"),
    path('feedback',views.feedback, name="feedback"),
    path('C',views.cpro, name="C"),
    path('office',views.office, name="office"),
    path('cf',views.cf, name="cf"),
    path('eng',views.eng, name="eng"),
    path('maths',views.maths, name="maths"),
    path('upload_notes',views.upload_notes, name="upload_notes"),

    ]
