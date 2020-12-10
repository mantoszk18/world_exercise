from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'api/city', views.CityViewSet)
router.register(r'api/continent', views.ContinentViewSet)
router.register(r'api/region', views.RegionViewSet)
router.register(r'api/country', views.CountryViewSet)
router.register(r'api/district', views.DistrictViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('api/continent/<continent>/regions/',
         views.ContinentRegionsView.as_view(),
         name='continent-regions'),
]
