from django.contrib import admin
from .models import Post, Tag, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
