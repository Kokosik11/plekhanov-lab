from django.contrib import admin
from .models import Profile, Order, OrderItem

admin.site.register(Profile)

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['service']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['number', 'user', 'status']
	list_filter = ['status', 'created', 'updated']
	list_editable = ('status',)
	search_fields = ('user', 'status', 'number')
	inlines = [OrderItemInline]