from django.contrib import admin
from .models import proom,Contact,Reserve
# Register your models here.
@admin.register(proom)
class proomAdmin(admin.ModelAdmin):
    list_display=['id','img','price','service']

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','message']    

@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display=['id','Adate','ddate','room','guest','email']    