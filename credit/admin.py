from django.contrib import admin

# Register your models here.

from .models import Client, Account, Credit

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Credit)