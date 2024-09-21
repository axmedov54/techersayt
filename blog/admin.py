from django.contrib import admin
from .models import *


admin.site.register(Matematika)

admin.site.register(Onnatili)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'narxi')  
#     list_filter = ('narxi',) 
#     search_fields = ('title', 'body') 


