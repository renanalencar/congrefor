# -*- coding: utf-8 -*-

from django.db import models

from account.models import Account

from django.utils.translation import ugettext_lazy as _

class Registration(Account):
    
    CATEGORY_LEVELS = [
        (1, u"Estudante/Profissional Não Graduado"),
        (2, u"Estudante de Pós-Graduação"),
        (3, u"Profissional Graduado"),
    ]
    
    category_level = models.IntegerField(_(u"Categoria"),choices=CATEGORY_LEVELS)
    
    payment = models.BooleanField(_("payment"), default=False)
    
    class Meta:
        #abstract = True
        Account._meta.get_field("user").verbose_name = u"Usuário"
        Account._meta.get_field("timezone").verbose_name = u"Fuso Horário"
        Account._meta.get_field("language").verbose_name = u"Idioma"