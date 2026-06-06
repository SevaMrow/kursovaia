from django import forms
from .models import Order, Client, Product, Equipment, ProductionStage

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'quantity', 'format', 'paper_type', 'deadline_date', 'status']
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'format': forms.TextInput(attrs={'class': 'form-control'}),
            'paper_type': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'inn': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'base_material_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'base_time_norm_hours': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class StageForm(forms.ModelForm):
    class Meta:
        model = ProductionStage
        fields = ['equipment', 'stage_name', 'planned_start', 'planned_end']
        widgets = {
            'planned_start': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'planned_end': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'equipment': forms.Select(attrs={'class': 'form-control'}),
            'stage_name': forms.TextInput(attrs={'class': 'form-control'}),
        }