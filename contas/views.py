from django.shortcuts import render
from .models import Transacao

def home(request):
    data = {}
    data['trasacoes'] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)