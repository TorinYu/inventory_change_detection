#coding=utf-8
from django import forms
from django.forms import FileInput

class UploadImageForm(forms.Form):
    photo1 = forms.FileField(widget=FileInput(), required=False)
    photo2 = forms.FileField(widget=FileInput(), required=False)
    def clean(self):
		cleaned_data = super(UploadImageForm, self).clean()
 		return self.cleaned_data