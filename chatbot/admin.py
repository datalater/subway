from django.contrib import admin

from .models import Line,Station,Recent,User,Schedule,Data
# Register your models here.

admin.site.register(Line)
admin.site.register(Station)
admin.site.register(Schedule)
admin.site.register(User)
admin.site.register(Data)
admin.site.register(Recent)