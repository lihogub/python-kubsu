from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import CodexForm, SubjectForm, LawForm
from .models import Law, Codex, Subject


def index(request):
    return HttpResponse("GG")


def lawById(request, lawId):
    law = get_object_or_404(Law, pk=lawId)
    context = {'law': law}
    return render(request, 'law.html', context)


def codexView(request):
    context = {}

    if request.method == 'GET':
        context['form'] = CodexForm()
        context['codex_list'] = Codex.objects.all()
    elif request.method == 'POST':
        form = CodexForm(request.POST)
        form.save()
        return HttpResponseRedirect('/codex')

    return render(request, 'codex.html', context)


def codexByIdView(request, codexId):
    context = {}

    if request.method == 'GET':
        codex = get_object_or_404(Codex, pk=codexId)
        context['form'] = CodexForm(instance=codex)
        context['codexId'] = codexId
        context['codex_list'] = Codex.objects.all()
    elif request.method == 'POST':
        codex = get_object_or_404(Codex, pk=codexId)
        form = CodexForm(request.POST, instance=codex)
        form.save()
        return HttpResponseRedirect('/codex')

    return render(request, 'codex.html', context)


def deleteCodexByIdView(request, codexId):
    codex = get_object_or_404(Codex, pk=codexId)
    codex.delete()
    return HttpResponseRedirect('/codex')


def subjectView(request):
    context = {}

    if request.method == 'GET':
        context['form'] = SubjectForm()
        context['subject_list'] = Subject.objects.all()
    elif request.method == 'POST':
        form = SubjectForm(request.POST)
        form.save()
        return HttpResponseRedirect('/subject')

    return render(request, 'subject.html', context)


def subjectByIdView(request, subjectId):
    context = {}

    if request.method == 'GET':
        subject = get_object_or_404(Subject, pk=subjectId)
        context['form'] = SubjectForm(instance=subject)
        context['subjectId'] = subjectId
        context['subject_list'] = Subject.objects.all()
    elif request.method == 'POST':
        subject = get_object_or_404(Subject, pk=subjectId)
        form = SubjectForm(request.POST, instance=subject)
        form.save()
        return HttpResponseRedirect('/subject')

    return render(request, 'subject.html', context)


def deleteSubjectByIdView(request, subjectId):
    subject = get_object_or_404(Subject, pk=subjectId)
    subject.delete()
    return HttpResponseRedirect('/subject')


def lawView(request):
    context = {}

    if request.method == 'GET':
        context['form'] = LawForm()
        context['law_list'] = Law.objects.all()
    elif request.method == 'POST':
        form = LawForm(request.POST)
        form.save()
        return HttpResponseRedirect('/law')

    return render(request, 'law.html', context)


def lawByIdView(request, lawId):
    context = {}

    if request.method == 'GET':
        law = get_object_or_404(Law, pk=lawId)
        context['form'] = LawForm(instance=law)
        context['lawId'] = lawId
        context['law_list'] = Law.objects.all()
    elif request.method == 'POST':
        law = get_object_or_404(Law, pk=lawId)
        form = LawForm(request.POST, instance=law)
        form.save()
        return HttpResponseRedirect('/law')

    return render(request, 'law.html', context)


def deleteLawByIdView(request, lawId):
    law = get_object_or_404(Law, pk=lawId)
    law.delete()
    return HttpResponseRedirect('/law')
