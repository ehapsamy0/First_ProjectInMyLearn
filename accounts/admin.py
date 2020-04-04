from django.contrib import admin
from . import models

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','headline','join_date')
    list_filter = ('headline','join_date')
    search_fields = ('user__first_name','headline','bio')
    list_editable = ('headline',)





admin.site.register(models.Profile,ProfileAdmin)
