from django.contrib import admin

from .models import Main


class MainAdmin(admin.ModelAdmin):
    list_display = ("name","experience","phone","address")


admin.site.register(Main, MainAdmin)