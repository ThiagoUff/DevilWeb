from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from Trabalho_5_devWeb import settings
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id','nome', 'email', 'cpf', 'endereco', 'data_cadastro')
        # <input type="hidden" name="User_id" id="id_User_id" value="xxx">

    id = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=False)

    # <input type="hidden" name="User_id" id="id_User_id" value="xxx">


    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    # <input type="text"
    #        name="nome"
    #        id="id_nome"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    email = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),

        required=True)

    # <input type="text"
    #        name="email"
    #        id="id_email"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    cpf = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),

        required=True)

    # <input type="text"
    #        name="cpf"
    #        id="id_cpf"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    endereco = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),

        required=True)

    # <input type="text"
    #        name="endereco"
    #        id="id_endereco"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    # <input type="text"
    #        name="preco"
    #        id="id_preco"
    #        class="form-control form-control-sm"
    #        min_length="4"
    #        maxlength="10"
    #        onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44')
    #        required>

    data_cadastro = forms.DateField(
        input_formats = settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    # <input type="text"
    #        name="data_cadastro"
    #        class="form-control form-control-sm hasDatepicker"
    #        required=""
    #        id="id_data_cadastro"
    #        maxlength="10">

class RemoveUserForm(forms.Form):
    class Meta:
        fields = ('id')

    id = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=False)
    # <input type="hidden" name="User_id" id="id_User_id" value="xxx">