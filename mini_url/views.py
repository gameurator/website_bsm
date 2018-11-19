from django.shortcuts import render, get_object_or_404, redirect
from .models import MiniURL
from .forms import MiniURLForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import resolvers


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


class URLCreate(CreateView):
    model = MiniURL
    form_class = MiniURLForm
    success_url = reverse_lazy(view_urls)
    # template_name = 'mini_url/miniurl_form.html'
    # fields = ['url', 'pseudo']


class URLUpdate(UpdateView):
    model = MiniURL
    form_class = MiniURLForm
    success_url = reverse_lazy(view_urls)
    template_name = 'mini_url/miniurl_update_form.html'

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniURL, code=code)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre URL a été mise à jour avec succès !")
        return HttpResponseRedirect(self.get_success_url())

class URLDelete(DeleteView):
    model = MiniURL
    success_url = reverse_lazy(view_urls)
    template_name = 'mini_url/supprimer.html'
