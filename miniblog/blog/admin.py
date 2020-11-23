from django.contrib import admin
from.models import blog,contact
# Register your models here.
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display=('id','title','desc')

@admin.register(contact)
class blogAdmin(admin.ModelAdmin):
    list_display=('id','name','email','message')

    
   