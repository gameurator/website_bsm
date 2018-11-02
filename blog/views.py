from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpRequest
from datetime import datetime
from blog.models import Article


# Create your views here.
def home(request):
    return HttpResponse("""
            <h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
        """)


def accueil(request: HttpRequest) -> HttpResponse:
    """Affiche tous les articles du blog"""
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {"tous_articles":articles})


def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    if id_article > 100:
        raise Http404
    article = Article.objects.get(id=id_article)
    return render(request, 'blog/afficher_article.html', {'article': article})


def list_articles(request: HttpRequest, month: int, year: int) -> HttpResponse:
    """ Liste des articles d'un mois précis. """
    if year < 2018:
        return redirect("https://www.djangoproject.com")
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)
    )


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
