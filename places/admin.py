from django.contrib import admin
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
    autocomplete_fields = ('place',)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview', ]
    extra = 0

    def image_preview(self, obj):
        return format_html('<img src="{}" height={} />', mark_safe(obj.photo.url), 200)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [ImageInline, ]
