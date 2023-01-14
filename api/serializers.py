from rest_framework import serializers
from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ('id',)


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

    #Object Level Validation
    def validate(self, data):
        '''

        Object Level Validation for BrandSerializer

        '''
        print(data)
        country = data.get('country')
        name = data.get('name')

        if country.lower() == 'pakistan':
            raise serializers.ValidationError('Country should not be Pakistan')
        if name[0] != name[0].upper():
            raise serializers.ValidationError('First character should be in uppercase')
        return data


