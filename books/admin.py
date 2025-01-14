from django.contrib import admin

from books.models import AuthorModel, BookModel

admin.site.register(AuthorModel)


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    search_fields = ['title', 'author']
    list_filter = ['title', 'price', 'author']
