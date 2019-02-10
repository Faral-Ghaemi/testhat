from django.contrib import admin
from . import models
# Register your models here.
class CreditAdmin(admin.ModelAdmin):
    list_display = ('user','number')


admin.site.register(models.Credit, CreditAdmin)
