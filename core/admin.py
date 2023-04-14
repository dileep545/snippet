from django.contrib import admin
from core.models import Tag,Snippet

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
