from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ('updated', 'timestamp')
    list_display = ('title','updated')
    search_fields = ('title','content')

admin.site.register(Post, PostAdmin)