from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age",)
    search_fields = ("name", "age",)
    ordering = ("name", "age",)
    readonly_fields = ("id",)