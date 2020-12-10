from django.db import models


class Region(models.Model):
    """
    Region model contains denormalized continents for performance reasons.

    The model will not grow (and even if then minimally - maybe a region divide or rename).
    That's why it's better to hold all the continents inside it,
    since getting all continents list is efficient.
    On the other hand having a continent in a
    predicate does not require an additional join to a separate, albeit small, table.

    """
    Continents = models.TextChoices(
        'Continent',
        'AFRICA ANTARCTICA ASIA EUROPE NORTH_AMERICA OCEANIA SOUTH_AMERICA'
    )

    continent = models.CharField(max_length=15, choices=Continents.choices)
    region = models.CharField(max_length=30)


class Country(models.Model):
    """
    A model describing a country in a given region.

    Regarding capital field.
    This information could be represented as a boolean value in the City model,
    although it would be a very sparsely populated column then - inefficiently indexable.
    So even though we have circular reference here it's much easier to reference
    and more coupled with its country.

    """
    code = models.CharField(max_length=3, primary_key=True,
                            help_text='International 3 letter country code')
    short_code = models.CharField(max_length=2, unique=True,
                                  help_text='International 2 letter country code')
    name = models.CharField(max_length=60)
    region = models.ForeignKey(Region, related_name='countries',
                               on_delete=models.PROTECT, db_index=True)
    surface_area = models.PositiveIntegerField()
    independence_year = models.SmallIntegerField(null=True)
    population = models.PositiveBigIntegerField(default=0)
    life_expectancy = models.FloatField(null=True)
    GNP = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    local_name = models.CharField(max_length=50)
    government = models.CharField(max_length=50)
    head_of_state = models.CharField(max_length=40, null=True)

    capital = models.OneToOneField('City', related_name='parent_country',
                                   on_delete=models.SET_NULL, null=True)
    languages = models.ManyToManyField('Language', through='CountryLanguage')


class District(models.Model):
    """
    District is part of the country where the City lies.

    If there was more info related to districts, we could refactor this to be connected
    to the country and city to district.

    """
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    population = models.PositiveIntegerField()

    country = models.ForeignKey(Country, db_column='country_code', on_delete=models.CASCADE)


class Language(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


class CountryLanguage(models.Model):
    """
    A intermediate table between Languages and Countries.

    There can be more than one official language for a country (e.g. Switzerland)

    """
    country = models.ForeignKey(Country, db_column='country_code', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, db_column='language_name', on_delete=models.CASCADE)
    is_official = models.BooleanField()
    percentage = models.FloatField()
