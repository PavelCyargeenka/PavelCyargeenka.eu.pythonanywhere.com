from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='mp'),
    path('band/', views.BandView.as_view(), name='bnd'),
    path('discography/', views.DiscographyView.as_view(), name='dsc'),
    path('bio/', views.DPBio.as_view(), name='bio'),
    path('discography/<slug:slug>/', views.AlbumView.as_view(), name='alb'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
]

handler404 = views.pagenotfound
