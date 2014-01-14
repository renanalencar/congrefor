# -*- coding: utf-8 -*-

import datetime

from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from markitup.fields import MarkupField


class Speaker(models.Model):
    
    SESSION_COUNT_CHOICES = [
        (1, "One"),
        (2, "Two")
    ]
    
    user = models.OneToOneField(User, null=True, related_name="speaker_profile")
    name = models.CharField(_(u"Nome"), max_length=100, help_text=_(u"Como você gostaria que ele aparecesse no programa do congresso."))
    biography = MarkupField(_(u"Biografia"), blank=True, help_text=u"Um pouco sobre você. Edite usando <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/' target='_blank'>Markdown</a>.")
    photo = models.ImageField(_(u"Foto"), upload_to="speaker_photos", blank=True)
    annotation = models.TextField()  # staff only
    invite_email = models.CharField(max_length=200, unique=True, null=True, db_index=True)
    invite_token = models.CharField(max_length=40, db_index=True)
    created = models.DateTimeField(
        default = datetime.datetime.now,
        editable = False
    )
    
    def __unicode__(self):
        if self.user:
            return self.name
        else:
            return "?"
    
    def get_absolute_url(self):
        return reverse("speaker_edit")
    
    @property
    def email(self):
        if self.user is not None:
            return self.user.email
        else:
            return self.invite_email
    
    @property
    def all_presentations(self):
        presentations = []
        if self.presentations:
            for p in self.presentations.all():
                presentations.append(p)
            for p in self.copresentations.all():
                presentations.append(p)
        return presentations
