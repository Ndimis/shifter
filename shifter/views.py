from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/accounts/login/'  # URL de redirection si l'utilisateur n'est pas authentifié
    redirect_field_name = 'redirect_to'  # Paramètre pour l'URL de redirection
