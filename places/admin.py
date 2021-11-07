from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


#admin.site.register(Place)
admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview",]

    def image_preview(self, obj):
        return format_html('<img src="{url}" height={height} />'.format(
            url = obj.photo.url,
            height=min(obj.photo.height, 200)))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]