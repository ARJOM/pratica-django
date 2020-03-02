from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm


def home(request):
    data = {}
    data['trasacoes'] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')
    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    data = {}

    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('list')
    data['form'] = form
    return render(request, 'contas/update.html', data)