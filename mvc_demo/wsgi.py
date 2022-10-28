"""ไฟล์ที่ใช้เก็บข้อมูลของ Django project ของเรา ใช้สำหรับการ deploy project เมื่อต้องการเชื่อมต่อกับ Web Server"""
"""
WSGI config for mvc_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mvc_demo.settings')

application = get_wsgi_application()
