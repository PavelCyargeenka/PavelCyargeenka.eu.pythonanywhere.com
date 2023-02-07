from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    site = models.URLField(default='')
    slug = models.SlugField(default='', null=False, db_index=True)
    portrait = models.ImageField(upload_to='portraits', default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Band, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# one to many
class Mark(models.Model):
    BAND_MEMBERS_CHOICES = [
        ('RE', 'Rod Evans'),
        ('IG', 'Ian Gillan'),
        ('DC', 'David Coverdale'),
        ('JLT', 'Joe Lynn Turner'),
        ('RB', 'Ritchie Blackmore'),
        ('TB', 'Tommy Bolin'),
        ('JS', 'Joe Satriani'),
        ('SM', 'Steve Morse'),
        ('SMB', 'Simon McBride'),
        ('NS', 'Nick Simper'),
        ('RG', 'Roger Glover'),
        ('GH', 'Glenn Hughes'),
        ('JL', 'Jon Lord'),
        ('DA', 'Don Airey'),
        ('IP', 'Ian Paice'),
    ]
    number = models.CharField(max_length=5)
    vocals = models.CharField(max_length=3, choices=BAND_MEMBERS_CHOICES, default='IG')
    guitar = models.CharField(max_length=3, choices=BAND_MEMBERS_CHOICES, default='RB')
    keyboards = models.CharField(max_length=3, choices=BAND_MEMBERS_CHOICES, default='JL')
    bass = models.CharField(max_length=3, choices=BAND_MEMBERS_CHOICES, default='RG')
    drums = models.CharField(max_length=3, choices=BAND_MEMBERS_CHOICES, default='IP')
    mark_foto = models.ImageField(upload_to='mark_foto', default='')

    def __str__(self):
        return f'Mark {self.number}'


# альбом
class Discography(models.Model):
    album_title = models.CharField(max_length=100)
    album_year = models.IntegerField(validators=[MinValueValidator(1968), MaxValueValidator(2023)])
    mark = models.ForeignKey(Mark, on_delete=models.SET_NULL, related_name='albums', null=True)
    slug = models.SlugField(default='', null=False, db_index=True)
    cover = models.ImageField(upload_to='covers', default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.album_title)
        super(Discography, self).save(*args, **kwargs)

    def __str__(self):
        return self.album_title


# песни из альбома
class Albums(models.Model):
    album = models.ForeignKey(Discography, on_delete=models.SET_NULL, related_name='songs', null=True)
    song_number = models.IntegerField()
    song_title = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.song_title)
        super(Albums, self).save(*args, **kwargs)

    def __str__(self):
        return self.song_title


class Bio(models.Model):
    dp_bio = models.TextField(default='')

    def __str__(self):
        return 'About Deep Purple'
