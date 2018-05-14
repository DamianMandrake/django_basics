from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "timestamp")
    search_fields = ["content", "title"]

    class Meta:
        model = Post


# this lets the super user add data to the posts
admin.site.register(Post, PostAdmin)

