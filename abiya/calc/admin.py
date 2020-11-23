from django.contrib import admin
from.models import contact,menu,table,himg
# Register your models here.
@admin.register(contact)
class slideAdmin(admin.ModelAdmin):
    list_display=['id','name','message','email']

@admin.register(menu)
class menuAdmin(admin.ModelAdmin):
    list_display=('mname','mprice','mlogo')    

@admin.register(table)
class tableAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','date','time','number_Of_Members') 
   
@admin.register(himg)
class himgAdmin(admin.ModelAdmin):
    list_display=('id','img')