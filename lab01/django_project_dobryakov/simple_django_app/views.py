from django.shortcuts import render
from simple_django_app.models import Auto
from django.http import Http404

def show_auto(request, auto_id):
    try:
        auto = Auto.objects.get(pk=auto_id)
    except Auto.DoesNotExist:
        raise Http404("Auto does not exist")

    return render(request, 'auto.html', {'auto': auto})

