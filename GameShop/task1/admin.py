from django.contrib import admin

# Register your models here.

from .models import Buyer, Game, News, Vendor, Delivery, DeliveryDet

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited', )
    search_fields = ('title',)
    list_filter = ('size', 'cost', 'age_limited', )
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name', )
    list_filter = ('balance', 'age',)
    readonly_fields = ('balance',)
    list_per_page = 30

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date',)
    search_fields = ('title', 'date', )
    list_filter = ('date',)
    readonly_fields = ('date',)
    list_per_page = 10

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )
    list_per_page = 10

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('bill_no', 'date', 'vendor_id', )
    search_fields = ('bill_no', )
    list_filter = ('bill_no', 'date', 'vendor_id', )
    list_per_page = 10
