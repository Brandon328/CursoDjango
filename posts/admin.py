# Django
from atexit import register
from django.contrib import admin

# Posts models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_filter = (
        'created',
        'modified',
        )

    readonly_fields = ('created', 'modified')
