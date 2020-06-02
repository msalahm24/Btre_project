from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','photo','is_mvp')
    list_display_links = ('id','name')
    list_filter = ('name','id')
    list_editable = ('is_mvp',)
# Register your models here.
admin.site.register(Realtor,RealtorAdmin)
