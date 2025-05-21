from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Medicamento, Categoria
from .forms import ProdutoForm, MedicamentoForm
from django.contrib.auth.decorators import login_required

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
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})    

# Adicionar medicamento
@login_required
def adicionar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
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
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form})

# Excluir produto
@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('lista_produtos')

