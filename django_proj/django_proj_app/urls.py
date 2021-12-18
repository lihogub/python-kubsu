from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('codex/', views.codexView, name='codexView'),
    path('codex/<int:codexId>', views.codexByIdView, name='codexByIdView'),
    path('codex/<int:codexId>/delete', views.deleteCodexByIdView, name='deleteCodexByIdView'),
    path('subject/', views.subjectView, name='subjectView'),
    path('subject/<int:subjectId>', views.subjectByIdView, name='subjectByIdView'),
    path('subject/<int:subjectId>/delete', views.deleteSubjectByIdView, name='deleteSubjectByIdView'),
    path('law/', views.lawView, name='lawView'),
    path('law/<int:lawId>', views.lawByIdView, name='lawByIdView'),
    path('law/<int:lawId>/delete', views.deleteLawByIdView, name='deleteLawByIdView')
]
