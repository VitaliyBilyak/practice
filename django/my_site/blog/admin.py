from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags","date")
    list_display = ("title", "date","author",)
    prepopulated_fields = {"slug": ("title",)}

#class BookAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}
#    list_filter = ("author", "rating",)
#    list_display = ("title", "author",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
# Register your models here.
