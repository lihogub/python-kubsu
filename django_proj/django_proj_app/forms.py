from django.forms import ModelForm

from .models import Subject, Codex, Law


class CodexForm(ModelForm):
    class Meta:
        model = Codex
        fields = ['title']


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name']


class LawForm(ModelForm):
    class Meta:
        model = Law
        fields = ['text', 'codex', 'subject']
