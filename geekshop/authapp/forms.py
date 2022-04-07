import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authapp.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите ваше имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите вашу фамилию'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите ваш адрес эл.почты'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if re.search('[a-zA-Z0-9]', self.cleaned_data['first_name']):
            raise ValueError("Пожалуйста введите ваше имя на кириллице. Не используйте цифры без цифр")
        return first_name

    def clean_username(self):
        if not re.match('[a-zA-Z]', self.cleaned_data['username']):
            raise ValueError("Пожалуйста введите имя пользователя латинскими буквами")
        return self.cleaned_data['username']
