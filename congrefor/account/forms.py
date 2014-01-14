# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

import account.forms


class SignupForm(account.forms.SignupForm):
    
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    email_confirm = forms.EmailField(label="Confirmar Email")
    
    CATEGORY_LEVELS = [
        (0, u"-----"),
        (1, u"Estudante/Profissional Não Graduado"),
        (2, u"Estudante de Pós-Graduação"),
        (3, u"Profissional Graduado"),
    ]
    
    category_level = forms.ChoiceField(label=u"Categoria", 
                 choices=(CATEGORY_LEVELS), initial=0, required=True,)

    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        self.fields.keyOrder = [
            "email",
            "email_confirm",
            "first_name",
            "last_name",
            "category_level",
            "password",
            "password_confirm"
        ]
    
    def clean_email_confirm(self):
        email = self.cleaned_data.get("email")
        email_confirm = self.cleaned_data["email_confirm"]
        if email:
            if email != email_confirm:
                raise forms.ValidationError("Email address must match previously typed email address")
        return email_confirm


class LoginForm(account.forms.LoginForm):
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["remember"].label = "Lembrar de mim"
        

class LoginEmailForm(LoginForm):
        
    email = forms.EmailField(label=_("E-mail"))
    authentication_fail_message = _("The email address and/or password you specified are not correct.")
    identifier_field = "email"
    
    def __init__(self, *args, **kwargs):
        super(LoginEmailForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ["email", "password", "remember"]