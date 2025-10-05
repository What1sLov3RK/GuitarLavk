from django import forms
from .models import Categories, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryFilterForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'required': False})
    )

    class Meta:
        model = Categories
        fields = {'categories'}

    def __init__(self, *args, **kwargs):
        super(CategoryFilterForm, self).__init__(*args, **kwargs)
        self.fields ['categories'].queryset = Categories.objects.all()


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Input your username'}), error_messages={'required': 'Input your username'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Input your password'}), error_messages={'required': 'Input password password'})
    password2 = forms.CharField(label='Password verification',
                                widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Input your password again'}),
                                error_messages={'required': 'Input verification password'})
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Input your email'}), required=True, error_messages={'required': 'Input your email'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class OrderForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "Order-form"}),
        error_messages={'required': 'Please enter your first name'})
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "Order-form"}),
        required=False)
    telephone = forms.CharField(
        widget=forms.TextInput(attrs={'class': "Order-form"}),
        required=False)
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': "Order-form"}),
        required=False)
    comment = forms.CharField(
        widget=forms.TextInput(attrs={'class': "Order-form"}),
        required=False)

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "telephone", "address", "comment")
