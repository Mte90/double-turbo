import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()
from django.conf import settings

from django.contrib.auth.models import Group, User
from django.contrib.auth import get_user_model

User = get_user_model()

def setup_database():
    free, created = Group.objects.get_or_create(name='free')
    basic, created = Group.objects.get_or_create(name='basic')
    advanced, created = Group.objects.get_or_create(name='advanced')
    print("Groups created")

    if settings.DEBUG:
        with open("./api/mock_data/users.json", 'r') as file:
            users_data = json.load(file)

        for user_data in users_data:
            user, created = User.objects.get_or_create(username=user_data.get('nickname'))
            user.email = user_data.get('email')
            user.set_password(user_data.get('nickname'))
            if user_data.get('plan') == "free":
                user.groups.add(free)
            if user_data.get('plan') == "basic":
                user.groups.add(basic)
            if user_data.get('plan') == "advanced":
                user.groups.add(advanced)

            user.role = user_data.get('role')
            user.save()
    print("Database setup completed.")

if __name__ == "__main__":
    setup_database()
