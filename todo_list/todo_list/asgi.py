"""
ASGI config for todo_list project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys
from django.core.asgi import get_asgi_application

# add your project directory to the sys.path 
project_home = u'/home/kevin/django-docker-compose/todo_list'
if project_home not in sys.path:
    sys.path.append(project_home)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

application = get_asgi_application()
