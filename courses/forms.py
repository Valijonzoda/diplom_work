from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titles': 'Psh. Klasa 11 ose Klasa e Informatikes',
            'description':'Vendos nje pershkrim te shkurte te klases',
            'images':'Mund te vendosesh nje fotografi e klases ose mund te lihet bosh'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'titles', 'klasa', 'description', 'images_len']
        help_texts = {
            'titles': 'Psh. Matematika, Gjeografi etj',
            'description':'Vendos nje pershkrim te shkurte te lendes',
            'klasa':'Zhgjidhni klasen per te cilen do te krijoni lenden',
            'images_len':'Mund te vendosesh nje fotografi e lendes ose mund te lihet bosh'
        }
        labels = {
            'titles':'Titulli i lendes'
        }
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','titles', 'lenda', 'video_id', 'positions', ]
        help_texts = {
            'titles':'Vendosni titlesn e mesimit',
            'lenda':'Zgjidhni lenden per te cilen i perket ky mesim',
            'video_id':'Vendosni ID e videos nga Youtube te cilen do te ngarkoni (<a href="/media/youtube_help.png">ku mund ta gjej ID</a>)',
            'positions':'Vendosni numrin e positionst ose radhen e mesimit '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }