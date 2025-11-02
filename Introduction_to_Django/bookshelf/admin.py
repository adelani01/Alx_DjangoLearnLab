from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Fields to show in list view
    list_display = ('title', 'author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')

    # Add filters in the sidebar
    list_filter = ('publication_year', 'author')



admin.site.register(Book,BookAdmin)
