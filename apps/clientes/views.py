from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import ClienteForm
from .models import Cliente


def novo_cliente(request):

    clientes = Cliente.objects.all()

    template_name = 'novo_cliente.html'
    context = {}

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('novo_cliente')
            return HttpResponse('<h1>Cliente cadastrado com sucesso!</h1>')

        else:
            return HttpResponse('<h1>Deu erro no formulário</h1>')

    form = ClienteForm()

    context['form'] = form
    context['clientes'] = clientes

    return render(request, template_name, context)

def atualizar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return HttpResponse('<h1>Cliente não encontrado</h1>')

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')
        else:
            return HttpResponse('<h1>Erro na atualização do cliente</h1>')
    
    form = ClienteForm(instance=cliente)
    template_name = 'novo_cliente.html'
    cliente = Cliente.objects.all()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def excluir_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
    except Cliente.DoesNotExist:
        return HttpResponse('<h1>Erro ao excluir o cliente. Não encontrado</h1>')
    return redirect('novo_cliente')

def login_usuario(request):
    template_name = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('novo_cliente')
        else:
            return HttpResponse(request, 'Usuário ou senha inválidos')
    else:
        form = ArithmeticError()

    context = {'form':form}
    return render(request, template_name, context)