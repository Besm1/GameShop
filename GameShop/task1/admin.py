from django.contrib import admin

# Register your models here.

from .models import Buyer, Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    search_fields = ('title',)
    list_filter = ('size', 'cost',)
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name', )
    list_filter = ('balance', 'age',)
    readonly_fields = ('balance',)
    list_per_page = 30
