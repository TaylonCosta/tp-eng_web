from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

from django.http import HttpResponse

def index (request):

    return render(request, "Monitore/index.html")

def monitorias (request):

    Monitoria = monitoria.objects.all()

    return render (request, 'Monitore/monitoria-list.hmtl', Monitoria)



def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'registration/register.html', context)

def CriarProduto (request):

    form = MonitoriaForm()
    if request.method == 'POST':
        form = MonitoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto')
    context = {'form': form}

    return render(request, 'LogoAli/produto_form.html', context)

def UpdateProduto (request, pk):

    produto = monitoria.objects.get(id=pk)
    form = MonitoriaForm(instance=produto)

    if request.method == 'POST':
        form = MonitoriaForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto')

    context = {'form': form}
    return render(request, 'LogoAli/produto_form.html', context)

def DeleteProduto(request, pk):

    produto = monitoria.objects.get(id=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('monitoria')

    context = {'item': produto}

    return render(request, 'Monitoria/delete.html', context)

def DetailProduto (request, pk):

    produtos = monitoria.objects.get(id=pk)

    context ={'produtos': produtos}

    return render(request, 'LogoAli/Produto_detail.html', context)
