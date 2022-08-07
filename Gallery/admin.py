from django.contrib import admin

from .models import Programs, PostImage, Mentor


# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Programs)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Programs


# @admin.register(PostImage)

class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mentor)
