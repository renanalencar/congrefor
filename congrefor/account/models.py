#import datetime
#import operator
#import urllib

#from django.core.mail import send_mail
#from django.core.urlresolvers import reverse
#from django.db import models, transaction
#from django.db.models import Q
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.template.loader import render_to_string
#from django.utils import timezone, translation
#from django.utils.translation import gettext_lazy as _

#from django.contrib.auth.models import User, AnonymousUser
#from django.contrib.sites.models import Site

#import pytz

#from account import signals
#from account.conf import settings
#from account.fields import TimeZoneField
#from account.managers import EmailAddressManager, EmailConfirmationManager
#from account.signals import signup_code_sent, signup_code_used
#from account.utils import random_token

# -*- coding: utf-8 -*-

#from django.db import models

#from account.models import Account

#from django.utils.translation import ugettext_lazy as _


#class Account(Account):
    
#    CATEGORY_LEVELS = [
#        (0, u"-----"),
#        (1, u"Estudante/Profissional Não Graduado"),
#        (2, u"Estudante de Pós-Graduação"),
#        (3, u"Profissional Graduado"),
#    ]
    
#    category_level = models.IntegerField(_(u"Eixo Temático"),choices=CATEGORY_LEVELS)
#    payment = models.BooleanField(_("payment"), default=False)