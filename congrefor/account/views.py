# -*- coding: utf-8 -*-

import hashlib
import random

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import account.views
import symposion.views

import congrefor.account.forms


class SignupView(symposion.views.SignupView):
    
    class Meta:
        form_class = congrefor.account.forms.SignupForm


class LoginView(symposion.views.LoginView):

    class Meta:
        form_class = congrefor.account.forms.LoginEmailForm


class SettingsView(account.views.SettingsView):
    
    class Meta:
        form_class = congrefor.account.forms.SettingsForm

@login_required
def lista(request):
    lista_itens = Payment.objects.filter()
    return render(request, "lista.html", {'lista_itens': lista_itens})