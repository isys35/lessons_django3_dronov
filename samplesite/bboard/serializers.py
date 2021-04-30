"""
    Листинг 28.1 Сериализатор RubricSerializer
"""

from rest_framework import serializers
from .models import Rubric


class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = ('id', 'name')