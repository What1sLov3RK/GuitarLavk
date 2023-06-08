from django import forms
from .models import Categories, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryFilterForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'required':False})
    )

    class Meta:
        model = Categories
        fields = {'categories'}

    def __init__(self, *args, **kwargs):
        super(CategoryFilterForm, self).__init__(*args, **kwargs)
        self.fields['categories'].queryset = Categories.objects.all()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password verification', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', required=True)


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class OrderForm(forms.Form):
    first_name = forms.CharField(widget=forms.Textarea)
    last_name = forms.CharField(widget=forms.Textarea)
    telephone = forms.CharField(widget=forms.Textarea)
    address = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "telephone", "address", "comment")