from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from service.models import DishType, Dish, Cook


@admin.register(DishType)
class DishType(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Dish)
class Dish(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["price"]
    list_display = ("name", "price", "description")


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": (
            "years_of_experience",
            "first_name",
            "last_name"
        )}),
    )
