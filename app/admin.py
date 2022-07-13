from django.contrib import admin
from app.models import Ask_it

class Ask_itAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ask_it, Ask_itAdmin)
