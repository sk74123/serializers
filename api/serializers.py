from rest_framework import serializers
from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'country', 'founded']


    # Field Level Validation
    def validate_founded(self, value):
        '''

        Field Level Validation for Brand Serializer

        '''

        print('value', value)
        min_year = 1880
        max_year = 2022
        if value <= min_year:
            raise serializers.ValidationError(f'Year should not be before {min_year}')

        if value > max_year:
            raise serializers.ValidationError(f'Year should not be after {max_year}')

        return value



