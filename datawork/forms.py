from django.db.models import fields
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class categoryForms(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('cat_doc', )


class brandfForms(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ('brand_doc', )



class sizeForms(forms.ModelForm):
    class Meta:
        model = Size
        exclude = ('size_doc', )



class thicknessForms(forms.ModelForm):
    class Meta:
        model = Thickness
        fields = "__all__"



class productForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('doc', 'issue', 'stock', )


# class CreateUserForms(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#         widgets = {
#             'username': forms.TextInput(attrs={"class":"form-control"}),
#             'email': forms.EmailInput(attrs={"class":"form-control"}),
#             'password1': forms.PasswordInput(attrs={"class":"form-control"}),
#             'password2': forms.PasswordInput(attrs={"class":"form-control"}),
#         }


class userForms(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    

class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('start_date', )


class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'