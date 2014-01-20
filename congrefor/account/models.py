# -*- coding: utf-8 -*-

from django.db import models

from account.models import Account as AccountBase
from account.models import EmailAddress

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

class Account(AccountBase):
    
    CATEGORY_LEVELS = [
        (1, u"Estudante/Profissional Não Graduado"),
        (2, u"Estudante de Pós-Graduação"),
        (3, u"Profissional Graduado"),
    ]
    
    category_level = models.IntegerField(_(u"Categoria"),choices=CATEGORY_LEVELS)
    
    class Meta:
        verbose_name = u"Contas"
        AccountBase._meta.get_field("user").verbose_name = u"Usuário"
        AccountBase._meta.get_field("timezone").verbose_name = u"Fuso Horário"
        AccountBase._meta.get_field("language").verbose_name = u"Idioma"

class Payment(models.Model):
    
    date = models.DateField(_(u"Data"))
    time = models.TimeField(_(u"Hora"))
    note = models.TextField(_(u"Observação"))
    confirmation = models.BooleanField(_(u"Pagamento"), default=False, help_text=_(u"Clique aqui para confirmar o pagamento da inscrição."))
    #user = models.OneToOneField(User, null=True, blank=True, verbose_name='Usuário')
    email = models.OneToOneField(EmailAddress, null=True, blank=True, verbose_name='Usuário')
    class Meta:
         verbose_name = u"Pagamento"
    
    def __unicode__(self):
        return unicode(self.email)