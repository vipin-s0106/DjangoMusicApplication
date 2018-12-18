from django.contrib import admin
from .models import Album, Song

#Register those model which you want to see in Admin Page
admin.site.register(Album)
admin.site.register(Song)
