from django.shortcuts import render, get_object_or_404, redirect
from .models import MiniURL
from .forms import MiniURLForm


# Create your views here.
def view_urls(request):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    urls = MiniURL.objects.all()
    return render(request, 'mini_url/view_urls.html', {'urls': urls})


def form_mini_url(request):
    form = MiniURLForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'mini_url/mini_url_formulaire.html', locals())


def redirect_url(request, code):
    """ Redirection vers l'URL enregistrée """
    mini = get_object_or_404(MiniURL, code=code)
    mini.count_access += 1
    mini.save()
    return redirect(mini.url, permanent=True)