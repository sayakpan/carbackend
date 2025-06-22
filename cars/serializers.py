from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'fuel_type', 'price', 'status']

    def validate_year(self, value):
        if value < 1000 or value > 9999:
            raise serializers.ValidationError("Year must be a 4-digit number.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value