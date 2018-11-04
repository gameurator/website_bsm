from django.contrib import admin
from .models import Categorie, Article


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')

    # Configuration du formulaire d'édition

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', ],
            'fields': ('titre', 'auteur', 'categorie', 'slug')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu',)
        }),
    )

    prepopulated_fields = {'slug': ('titre',), }
    # Colonnes personnalisées
    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article. S'il y a plus de 40 caractères, il faut rajouter
        des points de suspension.
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s…' % text
        else:
            return text
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
