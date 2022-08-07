from django.contrib import admin

from .models import Innovation,InnovativeImages

# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = InnovativeImages
    
@admin.register(Innovation)

class InnovationAdmin(admin.ModelAdmin):
    inlines=[PostImageAdmin]
    
    class Meta:
        model = Innovation
        
#@admin.register(InnovativeImages)

class PostImageAdmin(admin.ModelAdmin):
    pass