from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Medicamento, Categoria
from .forms import ProdutoForm, MedicamentoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

# Página inicial
def pagina_inicial(request):
    return render(request, 'estoque/home.html')

# Lista de produtos com busca
@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    busca = request.GET.get('buscar')
    if busca:
        produtos = produtos.filter(nome__icontains=busca)
    produtos = produtos.order_by('nome')
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

# Adicionar produto
@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            tamanho = form.cleaned_data['tamanho']
            categoria = form.cleaned_data['categoria']
            data_validade = form.cleaned_data['data_validade']
            ultima_compra = form.cleaned_data['ultima_compra']

            # Verifica se já existe produto exatamente igual
            if Produto.objects.filter(
                nome=nome, 
                tamanho=tamanho,
                categoria=categoria,
                data_validade=data_validade,
                ultima_compra=ultima_compra
            ).exists():
                messages.error(request, 'Produto já cadastrado com todas as mesmas informações!')
            else:
                try:
                    form.save()
                    messages.success(request, 'Produto cadastrado com sucesso!')
                    return redirect('lista_produtos')
                except IntegrityError:
                    messages.error(request, 'Erro ao salvar: produto já existe.')
    else:
        form = ProdutoForm()

    return render(request, 'estoque/adicionar_produto.html', {'form': form})

# Adicionar medicamento
@login_required
def adicionar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            tamanho = form.cleaned_data['tamanho']
            categoria = form.cleaned_data['categoria']
            data_validade = form.cleaned_data['data_validade']
            ultima_compra = form.cleaned_data['ultima_compra']
            dosagem = form.cleaned_data['dosagem']

            # Verifica se já existe medicamento exatamente igual
            if Medicamento.objects.filter(
                nome=nome,
                tamanho=tamanho,
                categoria=categoria,
                data_validade=data_validade,
                ultima_compra=ultima_compra,
                dosagem=dosagem
            ).exists():
                messages.error(request, 'Medicamento já cadastrado com todas as mesmas informações!')
            else:
                try:
                    form.save()
                    messages.success(request, 'Medicamento cadastrado com sucesso!')
                    return redirect('lista_produtos')
                except IntegrityError:
                    messages.error(request, 'Erro ao salvar: medicamento já existe.')
    else:
        form = MedicamentoForm()

    categorias = Categoria.objects.all()

    return render(request, 'estoque/adicionar_medicamento.html', {
        'form': form,
        'categorias': categorias
    })

# Editar produto
@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Produto editado com sucesso!')
                return redirect('lista_produtos')
            except IntegrityError:
                messages.error(request, 'Erro ao editar: produto já existe com essas informações.')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form})

# Excluir produto
@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    messages.success(request, 'Produto excluído com sucesso!')
    return redirect('lista_produtos')
