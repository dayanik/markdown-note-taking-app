from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('{<int:note_id>', views.get_note, name="get_note"),
    path('<int:note_id>/text', views.get_html, name="get_html"),
    path('<int:note_id>/check_grammar', views.check_note_grammar, name="check_note_grammar"),
    path('{/check_grammar', views.check_md_grammar, name="check_md_grammar"),
    path('{/upload', views.upload_note, name="upload_note"),
]
