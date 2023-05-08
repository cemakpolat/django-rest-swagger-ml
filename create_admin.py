import os
import django
from django.contrib.auth.management.commands.createsuperuser import get_user_model
from django.core.management import call_command

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot.settings')
django.setup()

# Create superuser if it doesn't exist
User = get_user_model()
try:
    User.objects.create_superuser('admin', 'admin@example.com', 'password')
except:
    pass
