from django.contrib import admin

from .models import Subway,User,Schedule,Data
# Register your models here.

admin.site.register(Subway)
admin.site.register(Schedule)
admin.site.register(User)
admin.site.register(Data)