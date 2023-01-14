from rest_framework import serializers
from .models import Brand


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    country = serializers.CharField(max_length=128)
    founded = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.founded = validated_data.get('founded', instance.founded)
        instance.save()
        return instance

    # Field Level Validation
    def validate_founded(self, value):
        print(value)
        if value <= 1947:
            raise serializers.ValidationError('Kindly add year after 1947')
        return value

    #Object Level Validation
    def validate(self, data):
        print(data)
        country = data.get('country')
        name = data.get('name')

        if country.lower() == 'pakistan':
            raise serializers.ValidationError('Country should not be Pakistan')
        if name[0] != name[0].upper():
            raise serializers.ValidationError('First character should be in uppercase')
        return data

