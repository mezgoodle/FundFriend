from django.contrib import admin

from core.document.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass
