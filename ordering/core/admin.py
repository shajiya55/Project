from django.contrib import admin
from .models import limit,market,stop
# Register your models here.
@admin.register(limit)
class limitAdmin(admin.ModelAdmin):
    list_display=['id','price','amount']

@admin.register(market)
class marketAdmin(admin.ModelAdmin):
    list_display=['id','amount']  

@admin.register(stop)
class stopAdmin(admin.ModelAdmin):
    list_display=['id','trigger_price']
