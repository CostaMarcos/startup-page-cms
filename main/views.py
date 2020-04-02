from django.shortcuts import render
from .models import All


def index(request):
    data = {}
    data['infos'] = All.objects.all()
    return render(request, 'main/index.html', data)
