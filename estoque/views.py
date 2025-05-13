from django.shortcuts import render, redirect
from .models import Produto, Medicamento
from .forms import ProdutoForm, MedicamentoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

@login_required
def adicionar_produto(request):
    # Lógica para adicionar produto
    return render(request, 'estoque/adicionar_produto.html')

@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    # Lógica para editar produto
    return render(request, 'estoque/editar_produto.html', {'produto': produto})

@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    # Lógica para excluir produto
    return redirect('lista_produtos')




#Pagina inicial
def pagina_inicial(request):
    return render(request, 'estoque/home.html')

# lista de produtos
def lista_produtos(request):
    # Obtém todos os produtos
    produtos = Produto.objects.all()
    # Verifica se há algum parâmetro de busca na URL
    busca = request.GET.get('buscar')
    if busca:
       produtos = produtos.filter(nome__icontains=busca)
    #ordena os produtos por nome, mesmo que não haja busca
    produtos = produtos.order_by('nome')
    # Renderiza o template com a lista de produtos (e resultado da pesquisa, se houver)
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

# adicionar Produtos
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})    
       
# adicionar medicamentos
def adicionar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = MedicamentoForm()
    return render(request, 'estoque/adicionar_medicamento.html', {'form': form})

#Editar produtos            
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

#Excluir produtos
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('lista_produtos')

# Create your views here.
