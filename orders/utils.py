from decimal import Decimal

def calculate_order_cost(order):
    """
    Расчёт себестоимости заказа
    Формула: (тираж * стоимость материалов на единицу) + (норма времени * стоимость машино-часа)
    """
    product = order.product
    quantity = order.quantity
    
    # Стоимость материалов
    material_cost = product.base_material_cost * quantity
    
    # Трудозатраты (норма времени * стоимость машино-часа)
    # Для простоты используем среднюю ставку оборудования
    hourly_rate = Decimal('1000')  # средняя ставка
    labor_cost = product.base_time_norm_hours * hourly_rate
    
    total = material_cost + labor_cost
    
    return total.quantize(Decimal('0.01'))