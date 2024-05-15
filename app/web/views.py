from django.views.generic import TemplateView, ListView
from .models import Slide, Service, Example, Achievement, Document, Project, Contact
from .forms import MyForm
from django.http import HttpResponse


class HomeView(ListView):
    template_name = "index.html"
    model = Example


class AchievementsView(ListView):
    template_name = "achievements.html"
    model = Achievement


class ContactsView(TemplateView):
    template_name = "contacts.html"
    

class ServicesView(ListView):
    template_name = "services.html"
    form_class = MyForm
    model = Service
    

class DocumentsView(ListView):
    template_name = "documents.html"
    model = Document
    

class ProjectsView(ListView):
    template_name = "projects.html"
    model = Project
    

class PrivacyView(TemplateView):
    template_name = "privacy.html"
    

def post(request):
    # получаем из данных запроса POST отправленные через форму данные

    Contact.objects.create(
        first_name=request.POST.get("first_name"),
        last_name=request.POST.get("last_name"),
        middle_name=request.POST.get("middle_name"),
        email=request.POST.get("email"),
        phone=request.POST.get("phone"),
        subject=request.POST.get("subject"),
        message=request.POST.get("message"),
        type=request.POST.get("type"),
        kindbusiness=request.POST.get("kindbusiness"),
        kindservice=request.POST.get("kindservice"),
    )


    return HttpResponse(f"<h2>Заявка успешно отправлена</h2>")