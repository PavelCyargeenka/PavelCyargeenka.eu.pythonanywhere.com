from welcome.models import Band, Discography, Mark, Bio
from django.views.generic import TemplateView, ListView, DetailView


class MainPage(TemplateView):
    template_name = 'welcome/welcome.html'


class BandView(ListView):
    model = Band
    template_name = 'welcome/band.html'
    context_object_name = 'members'


class DiscographyView(ListView):
    model = Discography
    template_name = 'welcome/discography.html'
    context_object_name = 'band_discography'

    def get_queryset(self):
        super(DiscographyView, self).get_queryset()
        qs_sorted = Discography.objects.order_by('album_year')
        return qs_sorted


class DPBio(TemplateView):
    template_name = 'welcome/bio.html'

    def get_context_data(self, **kwargs):
        context = super(DPBio, self).get_context_data()
        context['dp_bio'] = Bio.objects.get(id=1)
        return context


class AlbumView(DetailView):
    model = Discography
    template_name = 'welcome/album.html'
    context_object_name = 'this_album'


class GalleryView(ListView):
    model = Mark
    template_name = 'welcome/gallery.html'
    context_object_name = 'line_ups'


