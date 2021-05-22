from django.contrib import admin
from .models import Song ,watchlater , History
# Register your models here.

admin.site.register(Song)
admin.site.register(watchlater)
admin.site.register(History)