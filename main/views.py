from django.shortcuts import render
from .models import Header


def index(request):
    data = {}
    data['infos'] = Header.objects.all()
    return render(request, 'main/index.html', data)
