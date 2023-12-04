from django.contrib import admin

from core.bank.models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass
