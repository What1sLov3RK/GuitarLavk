from django.apps import AppConfig


class GuitarlavkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    filters = 'django_filters'
    name = 'guitarlavka'


class GuitarlavkaConfigdjango_filters(AppConfig):
    filters = 'django_filters'
    name = 'guitarlavka'
