from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название роли")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    inn = models.CharField(max_length=12, blank=True, verbose_name="ИНН")
    contact_person = models.CharField(max_length=100, blank=True, verbose_name="Контактное лицо")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    address = models.TextField(blank=True, verbose_name="Адрес")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование продукции")
    description = models.TextField(blank=True, verbose_name="Описание")
    base_material_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Базовая стоимость материалов")
    base_time_norm_hours = models.DecimalField(max_digits=8, decimal_places=2, default=1, verbose_name="Норма времени (часы)")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('print', 'Печатное'),
        ('cutting', 'Резальное'),
        ('binding', 'Брошюровочное'),
    ]
    name = models.CharField(max_length=100, verbose_name="Наименование")
    equipment_type = models.CharField(max_length=20, choices=EQUIPMENT_TYPES, default='print', verbose_name="Тип")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=1000, verbose_name="Стоимость машино-часа")
    is_available = models.BooleanField(default=True, verbose_name="Доступность")
    
    def __str__(self):
        return f"{self.name} ({'Доступно' if self.is_available else 'В ремонте'})"
    
    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название статуса")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"

class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True, verbose_name="Номер заказа")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукция")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Менеджер")
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name="Статус")
    quantity = models.IntegerField(verbose_name="Тираж")
    format = models.CharField(max_length=20, blank=True, verbose_name="Формат")
    paper_type = models.CharField(max_length=50, blank=True, verbose_name="Тип бумаги")
    deadline_date = models.DateField(verbose_name="Срок сдачи")
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Себестоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.order_number} - {self.client.name}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"ЗАК-{self.created_at.strftime('%Y%m%d%H%M%S') if self.created_at else '000'}"
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class ProductionStage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='stages', verbose_name="Заказ")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Оборудование")
    stage_name = models.CharField(max_length=100, verbose_name="Название этапа")
    planned_start = models.DateField(verbose_name="План. начало")
    planned_end = models.DateField(verbose_name="План. окончание")
    actual_start = models.DateField(null=True, blank=True, verbose_name="Факт. начало")
    actual_end = models.DateField(null=True, blank=True, verbose_name="Факт. окончание")
    stage_status = models.CharField(max_length=50, default='Запланирован', verbose_name="Статус этапа")
    
    def __str__(self):
        return f"{self.order.order_number} - {self.stage_name}"
    
    class Meta:
        verbose_name = "Этап производства"
        verbose_name_plural = "Этапы производства"

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('email', 'Email'),
        ('system', 'Системное'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Получатель")
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='system', verbose_name="Тип")
    message = models.TextField(verbose_name="Сообщение")
    is_sent = models.BooleanField(default=False, verbose_name="Отправлено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"Уведомление для {self.user.username} по заказу {self.order.order_number}"
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"