import datetime

from django import forms
from django.forms.widgets import Textarea

#TODO: ASK JM, is machine type (ex. Sparkle - Bravo) required?


class PipetteCheckForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=Textarea, required=False)
    type = forms.ChoiceField(choices=(('CLIA', 'CLIA'), ('R&D','R&D')))
    status = forms.ChoiceField(choices=(
        ('Pass QC', 'Pass QC Check'),
        ('Fail QC', 'Fail QC Check')))
    timestamp = forms.DateTimeField(initial=datetime.datetime.now,
        help_text="Type date/time in these formats to over-write: 2013-10-30, 10/30/13 14:30. Time is optional.")
    #TODO: fix this part
    date_files = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        self.datastore = kwargs.pop("datastore")
        super(PipetteCheckForm, self).__init__(*args, **kwargs)
