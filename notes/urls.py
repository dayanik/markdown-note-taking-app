from django.urls import path

from notes import views


urlpatterns = [
    path('', views.index, name="index"),
    path('{<int:note_id>}/download/', views.download_note, name="download"),
    path('{<int:note_id>}/text/', views.html_note, name="text")
]
