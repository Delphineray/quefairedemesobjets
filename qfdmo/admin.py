from django.contrib import admin

from .models import Category, SubCategory


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "code")
    search_fields = [
        "category__name",
        "code",
        "name",
    ]


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category)