from django import forms
from .models import Article


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir un copie du mail envoyé.", required=False)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
