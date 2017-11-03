from django.db import migrations
from django.conf import settings
from django.contrib.auth.hashers import make_password

def create_superuser_ifneeded(apps, sche):
    User = apps.get_model(settings.AUTH_USER_MODEL)

    try:
        User.objects.get(username=settings.SUPERUSER_NAME)
    except User.DoesNotExist:
        admin = User(
            username = settings.SUPERUSER_NAME,
            password = make_password(settings.SUPERUSER_PASSWORD),
            email='',
            is_staff = True,
            is_superuser = True,

        )
        admin.save()


def reverse_create_superuser(apps, sche):
    pass


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(create_superuser_ifneeded, reverse_create_superuser),
    ]
