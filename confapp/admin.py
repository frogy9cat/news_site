from django.contrib import admin
from .models import News, Category1, Authorization


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'info', 'category1', 'updated_at', 'created_at')
    list_display_links = ('title', 'info', 'category1')
    search_fields = ('title', 'category1')


admin.site.register(News, NewsAdmin)
admin.site.register(Category1)
admin.site.register(Authorization)