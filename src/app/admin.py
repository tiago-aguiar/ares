from django.contrib import admin

from .models import Post
from .models import Config
from .models import PostConfig
from .models import Source
from .models import ShortenerUrl


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["title"]
    list_filter = ["created_date"]
    search_fields = ["title"]


class ConfigAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    list_filter = ["created_date"]
    search_fields = ["name"]


class PostConfigAdmin(admin.ModelAdmin):
    pass


class SourceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "domain", "created_date"]
    list_display_links = ["name"]
    list_filter = ["created_date"]
    search_fields = ["name"]


class ShortenerUrlAdmin(admin.ModelAdmin):
    list_display = ["id", "source", "medium", "dest",
                    "shortcut", "link", "count", "created_date"]
    list_display_links = ["shortcut"]
    list_filter = ["medium", "source", "dest"]
    search_fields = ["link"]

    #  called on save at admin
    def save_model(self, request, obj, form, change):
        if obj.shortcut is None or obj.shortcut == "":
            obj.shortcut = ''.join(random.choice(string.ascii_letters)
                                   for x in range(6))

        if obj.dest.name == "Blog" and "utm_source" not in obj.link:
            obj.link = obj.link + "?utm_source=" + \
                obj.source.name.lower() + "&utm_medium=" + obj.medium.lower()
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(PostConfig, PostConfigAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ShortenerUrl, ShortenerUrlAdmin)
