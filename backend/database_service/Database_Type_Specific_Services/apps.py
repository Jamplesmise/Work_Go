from django.apps import AppConfig


class DatabaseTypeSpecificServicesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Database_Type_Specific_Services"
