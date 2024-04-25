from .models import Cat
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Cat
        fields = '__all__'