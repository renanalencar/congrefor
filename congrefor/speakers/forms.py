# -*- coding: utf-8 -*-

from django import forms

from markitup.widgets import MarkItUpWidget

from congrefor.speakers.models import Speaker


class SpeakerForm(forms.ModelForm):
    
    class Meta:
        model = Speaker
        fields = [
            "name",
            "biography",
            "photo",
        ]
        widgets = {
            "biography": MarkItUpWidget(),
        }
