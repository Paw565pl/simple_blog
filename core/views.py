from django.views.generic.base import TemplateView

# Create your views here.
class PageNotFoundView(TemplateView):
    template_name = "core/404.html"
