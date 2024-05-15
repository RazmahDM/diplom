from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("achievements/", views.AchievementsView.as_view()),
    path("contacts/", views.ContactsView.as_view()),
    path("projects/", views.ProjectsView.as_view()),
    path("services/", views.ServicesView.as_view()),
    path("documents/", views.DocumentsView.as_view()),
    path("privacy/", views.PrivacyView.as_view()),
    path("post/", views.post),
]