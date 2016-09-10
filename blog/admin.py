from django.contrib import admin
from .models import Post, PostImage
# Register your models here.


admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title']
	list_display_links = ['title']

admin.site.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'picture']
	list_display_links = ['picture']
