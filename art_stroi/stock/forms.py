from django import forms

from stock.models import Category


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}), label_suffix="")
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}), label_suffix="")


class ApplicationForm(forms.Form):
    name_of_manager = forms.CharField(label='Имя менеджера', widget=forms.TextInput(attrs={'class': 'form-input'}))
    title_of_product = forms.CharField(label='Наименование товара', widget=forms.TextInput(attrs={'class': 'form-input'}))
    amount_of_product = forms.IntegerField(label='Количество товара', widget=forms.TextInput(attrs={'class': 'form-control'}))
    characteristic_of_product = forms.CharField(label='Характеристика товара', required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))

