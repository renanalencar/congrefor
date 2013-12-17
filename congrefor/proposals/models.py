# -*- coding: utf-8 -*-

from django.db import models

from symposion.proposals.models import ProposalBase

from django.utils.translation import ugettext_lazy as _


class Proposal(ProposalBase):
    
    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3
    
    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, u"Ensino Médio Técnico"),
        (AUDIENCE_LEVEL_INTERMEDIATE, u"Ensino Superior"),
        (AUDIENCE_LEVEL_EXPERIENCED, "Profissional"),
    ]
    
    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)
    
    recording_release = models.BooleanField(
        default=True,
        help_text=_(u"Ao enviar sua proposta, você concorda em dar permissão para os organizadores do congresso para gravar, editar e lançar áudio e/ou vídeo de sua apresentação. Se você não concorda com isso, por favor, desmarque esta caixa.")
    )
    
    class Meta:
        abstract = True


class TalkProposal(Proposal):
    class Meta:
        verbose_name = "talk proposal"


class TutorialProposal(Proposal):
    class Meta:
        verbose_name = "tutorial proposal"
