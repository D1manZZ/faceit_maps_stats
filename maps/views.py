from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import LinkMatch
from .logic import logic

link = 'no_link'


class SetLink(FormView):

    template_name = 'maps/form.html'
    form_class = LinkMatch
    success_url = reverse_lazy('view_maps')

    def form_valid(self, form):
        global link
        link = form.cleaned_data['link']
        return super().form_valid(form)


class ViewMaps(TemplateView):

    template_name = 'maps/maps.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = logic(link)
        return context
