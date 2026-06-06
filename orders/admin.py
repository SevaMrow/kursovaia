from django.contrib import admin
from .models import Role, Client, Product, Equipment, OrderStatus, Order, ProductionStage, Notification

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'phone', 'email')
    search_fields = ('name', 'inn')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_material_cost', 'base_time_norm_hours')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment_type', 'hourly_rate', 'is_available')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'client', 'status', 'deadline_date', 'total_cost')
    list_filter = ('status', 'created_at')
    search_fields = ('order_number', 'client__name')

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProductionStage)
class ProductionStageAdmin(admin.ModelAdmin):
    list_display = ('order', 'stage_name', 'planned_start', 'planned_end', 'stage_status')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'message', 'is_sent', 'created_at')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)