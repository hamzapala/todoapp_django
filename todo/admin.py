from django.contrib import admin

from .models import Todos

# Register your models here.
class TodosAdmin(admin.ModelAdmin):
    list_display = ["title","is_done", "created_at","updated_at", "priority"]
    list_filter=("is_done",)


admin.site.register(Todos,TodosAdmin)