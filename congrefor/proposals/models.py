# -*- coding: utf-8 -*-

from django.db import models

from symposion.proposals.models import ProposalBase

from django.utils.translation import ugettext_lazy as _


class Proposal(ProposalBase):
    
    #AUDIENCE_LEVEL_NOVICE = 1
    #AUDIENCE_LEVEL_EXPERIENCED = 2
    #AUDIENCE_LEVEL_INTERMEDIATE = 3
    
    TOPIC_AREAS = [
        (1, u"Redes de Atenção à Saúde"),
        (2, u"Saúde Mental, Álcool, Crack e outras Drogas"),
        (3, u"Vigilância em Saúde"),
        (4, u"Experiências Pedagógicas Inovadoras"),
        (5, u"Etnia, Raça e Saúde"),
        (6, u"Educação Permanente em Saúde"),
        (7, u"Educação Popular em Saúde, mobilização, controle e participação social em experiências de formação"),
        (8, u"Formação em Residências para o SUS"),
    ]
    
    audience_level = models.IntegerField(_(u"Eixo Temático"),choices=TOPIC_AREAS)
    #topic_area = models.IntegerField(_(u"Eixo Temático"),choices=TOPIC_AREAS)
    
    recording_release = models.BooleanField(
        _(u"Liberação para gravação"),                                    
        default=True,
        help_text=_(u"Ao enviar sua proposta, você concorda em dar permissão para os organizadores do congresso para gravar, editar e lançar áudio e/ou vídeo de sua apresentação. Se você não concorda com isso, por favor, desmarque esta caixa.")
    )
    
    
    class Meta:
        abstract = True
        ProposalBase._meta.get_field("title").verbose_name = u"Título"
        
        ProposalBase._meta.get_field('description').verbose_name = u"Breve Resumo"
        ProposalBase._meta.get_field('description').help_text = u"Se a sua apresentação for aceita isso será tornado público e impresso no programa. Deve ser um parágrafo, no máximo 400 caracteres."
        
        ProposalBase._meta.get_field('abstract').verbose_name = u"Resumo Detalhado"
        ProposalBase._meta.get_field('abstract').help_text = u"Descrição detalhada e esboço. Isso será tornado público, se sua apresentação for aceita. Edite usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>."
        
        ProposalBase._meta.get_field('additional_notes').verbose_name = u"Observações"
        ProposalBase._meta.get_field('additional_notes').help_text = u"Qualquer outra informação que você gostaria que a comissão científica soubesse ao fazer a sua seleção: sua experiência passada como palestrante, as experiências relevantes deste trabalho, etc. Edite usando <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>."


class TalkProposal(Proposal):
    class Meta:
        verbose_name = "talk proposal"


class TutorialProposal(Proposal):
    class Meta:
        verbose_name = "tutorial proposal"
