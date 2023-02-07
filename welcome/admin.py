from django.contrib import admin
from .models import Discography, Mark, Band, Albums, Bio


@admin.register(Discography)
class DiscographyAdmin(admin.ModelAdmin):
    list_display = ['id', 'cover', 'album_title', 'album_year', 'mark']
    list_editable = ['cover', 'album_title', 'album_year', 'mark']
    ordering = ['album_year', 'id']
    search_fields = ['album_title', 'album_year']
    prepopulated_fields = {'slug': ('album_title',)}


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark_foto', 'number', 'vocals', 'guitar', 'bass', 'keyboards', 'drums']
    list_editable = ['mark_foto', 'number', 'vocals', 'guitar', 'bass', 'keyboards', 'drums']
    ordering = ['id']


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['id', 'portrait', 'name', 'instrument', 'site']
    list_editable = ['portrait', 'name', 'instrument', 'site']
    ordering = ['id']


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'song_number', 'song_title']
    list_editable = ['album', 'song_number', 'song_title']
    ordering = ['id']


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ['id', 'dp_bio']
    list_editable = ['dp_bio']

