from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from flower.models import *
from django import forms

class FlowerForm(forms.ModelForm):
    # name = forms.CharField(max_length=250, label='Название')
    # description = forms.CharField(label='Описание',widget=forms.Textarea())
    # slug = forms.SlugField(max_length=250, label='URL')
    # photo = forms.ImageField(label='Фото')
    # is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='категория не выбрана')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label='категория не выбрана'
        self.fields['is_published'].initial = True
        self.fields['is_published'].requared = False
    class Meta:
        model = Flower
        fields = '__all__'
        exclude = ['time_create', 'time_update']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols':50,'rows':10})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длинная строка')
        return  name

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField (label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class ConnectForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
    contact = forms.CharField(label='O себе', widget=forms.Textarea(attrs={'cols':50,'rows':10}))
    captcha = CaptchaField()