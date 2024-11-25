from django.apps import AppConfig
from user_management_project.settings import MONGO_DB


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # Ensure unique index on the email field
        MONGO_DB[self.name].create_index("email", unique=True)
    