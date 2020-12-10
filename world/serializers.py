from rest_framework import serializers

from .models import City, Country, Region, District


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.

    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Country
        fields = ['code', 'short_code', 'surface_area', 'name', 'independence_year',
                  'population', 'life_expectancy', 'GNP', 'local_name', 'government',
                  'head_of_state']


class RegionSerializer(serializers.ModelSerializer):
    countries = CountrySerializer(many=True, read_only=True, fields=('code', 'name'))

    class Meta:
        model = Region
        fields = ['region', 'countries']


class ContinentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['continent']
