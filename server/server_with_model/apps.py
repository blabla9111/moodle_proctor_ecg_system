from django.apps import AppConfig


class ServerWithModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server_with_model'
