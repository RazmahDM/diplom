from django.contrib import admin

# Register your models here.
from .models import Contact, Service, Example, Achievement, Document, Project


admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Example)
admin.site.register(Achievement)
admin.site.register(Document)
admin.site.register(Project)