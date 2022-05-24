from django.contrib import admin

from .models import Main


class MainAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)


admin.site.register(Main, MainAdmin)