from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин:', max_length=30, min_length=3, required=True)
    password = forms.CharField(label='Введите пароль:', widget=forms.PasswordInput(), min_length=8, strip=False, required=True)
    repeat_password = forms.CharField(label='Повторите пароль:', widget=forms.PasswordInput(), min_length=8, strip=False, required=True)
    age = forms.IntegerField(label='Укажите возраст:', min_value=18, max_value=120, required=True)
