from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers as world_serializers


class ContinentViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = world_serializers.ContinentSerializer
    queryset = models.Region.objects.order_by('continent').distinct('continent')


class ContinentRegionsView(generics.ListAPIView):

    serializer_class = world_serializers.RegionSerializer
    lookup_url_kwarg = 'continent'

    def get_queryset(self):
        continent = self.kwargs.get(self.lookup_url_kwarg)
        regions = models.Region.objects.filter(continent=continent).order_by('region')
        return regions


class RegionViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = world_serializers.RegionSerializer
    queryset = models.Region.objects.order_by('region').distinct('region')

    @action(detail=False)
    def continents_regions(self, request, continent=None):
        regions = models.Region.objects.filter(continent=continent)
        serializer = self.get_serializer(regions, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):

    serializer_class = world_serializers.CitySerializer
    queryset = models.City.objects.all()


class CountryViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = world_serializers.CountrySerializer
    queryset = models.Country.objects.all()


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = world_serializers.DistrictSerializer
    queryset = models.District.objects.all()
