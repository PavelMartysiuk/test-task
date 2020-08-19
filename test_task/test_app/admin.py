from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_name', 'description']
    list_display_link = ['title', ]
    search_fields = ['title', ]


admin.site.register(Book, BookAdmin)
# Register your models here.
