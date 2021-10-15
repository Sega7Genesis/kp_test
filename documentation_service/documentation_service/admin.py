from django.contrib import admin

from .models import Documentation


@admin.register(Documentation)
class DocumentationModelAdmin(admin.ModelAdmin):
    pass
