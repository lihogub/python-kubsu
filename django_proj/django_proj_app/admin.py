from django.contrib import admin
from .models import Codex, Subject, Law

# Register your models here.

admin.site.register(Codex)
admin.site.register(Subject)
admin.site.register(Law)
