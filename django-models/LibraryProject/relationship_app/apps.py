from django.apps import AppConfig
class DjangomodelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django-models'

    def ready(self):
        import relationship_app.signals
class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
