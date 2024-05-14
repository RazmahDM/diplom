from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class AchievementsView(TemplateView):
    template_name = "achievements.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"
    

class ServicesView(TemplateView):
    template_name = "services.html"
    

class DocumentsView(TemplateView):
    template_name = "documents.html"
    

class ProjectsView(TemplateView):
    template_name = "projects.html"
    

class PrivacyView(TemplateView):
    template_name = "privacy.html"
    