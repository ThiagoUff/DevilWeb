from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from Site.forms import UserForm,RemoveUserForm
from Site.models import Images, User


def home(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='Home'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    return render(request, 'Home/index.html',{'caminhos':caminhos} )


def noticia(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='Home_Bar'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='noticia'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    return render(request, 'Noticia/noticia.html', {'caminhos':caminhos})

def login(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    return render(request, 'login/login.html', {'caminhos':caminhos})



def cadastra_User(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='cadastro'):
        caminhos[item.nome] = "images/" + item.caminho
    # Aqui recuperamos o parâmetro de requisição produto_id.
    # Se este parâmetro de requisição existir no objeto request, significa que se trata de uma alteração.
    # Caso contrário, trata-se de uma inclusão.
    User_id = request.POST.get('id')
    print("User_id")
    print(User_id)
    if request.POST:
        # Se o parâmetro veio, trata-se de uma alteração.
        if User_id:
            acao = 'alteracao'
            # Recupera um objeto Produto ou gera o erro 404
            user = get_object_or_404(User, pk=User_id)

            # Como se trata de uma alteração, o objeto ProdutoForm é instanciado utilizando
            # os dados provenientes do banco de dados (instance=produto) e, em seguida,
            # essas informações são atualizadas utilizando os dados submetidos pelo usuário (request.POST).
            form_user = UserForm(request.POST, instance=user)
        else:

            acao = 'inclusao'
            form_user = UserForm(request.POST)

        # A linha de código abaixo testa se os dados constantes do form estão corretos.
        # As regras de validação foram definidas no form (ProdutoForm). Os campos categoria, nome, preco e
        # data_cadastro são de preenchimento obrigatório (required=True). E o campo preco deve obedecer a
        # uma expressão regular (veja em ProdutoForm)

        # Observe que o comando if abaixo não possui o "else". Caso ocorra um erro de validação a página
        # cadastra_produto.html será exibida novamente juntamente com as mensagens de erro.
        if form_user.is_valid():
            print("VALIDO")
            # O método save() de ModelForm salva o produto (inclui ou altera) no banco de dados e retorna
            # um objeto do tipo Produto.
            user = form_user.save()

            # Se a variável produto_id for diferente de None então trata-se de uma alteração
            if User_id:
                # Gera uma mensagem que será exibida pela página exibe_produto.html através do framework de mensagens.
                messages.add_message(request, messages.INFO, 'Usuário alterado com sucesso.')
            else:
                messages.add_message(request, messages.INFO, 'Usuário cadastrado com sucesso.')

            # Aqui efetuamos um redirect para evitar que um mesmo produto seja cadastrado mais
            # de uma vez caso o usuário aperte a tecla F5 após cadastrar o produto.
            return redirect('Site:exibe_user', id=user.id)
        else:
            print("NAO VALIDO")
            return render(request, 'Cadastro/cadastra_user.html',{'form': form_user, 'acao': acao, 'caminhos': caminhos})

    else:
        # Ao chegar uma requisição do tipo GET, a página cadastra_produto.html é exibida.
        acao = 'inclusao'

        form_user = UserForm()

    # Caso ocorra um erro de validação a página cadastra_produto.html será exibida com as
    # mensagens de erro de validação.
    return render(request, 'Cadastro/cadastra_user.html', {'form': form_user, 'acao': acao,'caminhos':caminhos})


def exibe_user(request, id):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='exibir'):
        caminhos[item.nome] = "images/" + item.caminho
    user = get_object_or_404(User, pk=id)
    # Aqui instanciamos o objeto remove_produto_form para que os botões de edição e de remoção sejam exibidos.
    return render(request, 'Cadastro/exibe_usuario.html', {'user': user,'remove_user_form': id,'caminhos':caminhos})


def edita_user(request, id):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='cadastro'):
        caminhos[item.nome] = "images/" + item.caminho
    user = get_object_or_404(User, pk=id)
    form_user = UserForm(instance=user)
    form_user.fields['id'].initial = user.id
    return render(request, 'Cadastro/cadastra_user.html', {'form': form_user,'acao': 'alteracao','caminhos':caminhos})


def remove_user(request):
    print("REMOVE")
    User_id = request.POST.get('User_id')
    print(User_id)
    remove_user_form = RemoveUserForm(request.POST)
    if remove_user_form.is_valid():
        print("REMOVE2")

        print("REMOVE3")
        user = get_object_or_404(User, pk=User_id)
        print("REMOVE4")
        user.delete()
        print("REMOVE5")
        messages.add_message(request, messages.INFO, 'Usuário removido com sucesso.')
        return render(request, 'Cadastro/exibe_usuario.html', {'user': user, 'remove_usuario_form': None})
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar remover um Usuário')



