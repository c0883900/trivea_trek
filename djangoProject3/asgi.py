"""
Team Members
Manmeet Kaur - C0884039
Angrej Singh - C0884026
Riya Sidhu - C0886435
Dheepasri Ravichandran - C0883900
ASGI config for djangoProject3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject3.settings')

application = get_asgi_application()
