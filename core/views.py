from django.views.generic.base import TemplateView


# Create your views here.
class PageNotFoundView(TemplateView):
    template_name = "core/404.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)
