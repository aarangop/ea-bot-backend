from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['permalink', 'hit_or_miss']
    list_filter = ['hit_or_miss']
