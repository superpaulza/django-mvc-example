"""
This file like a database of Django store an init value before the program started
ไฟล์ที่ใช้เก็บ configuration ทั้งหมดของ project เอาไว้
เช่น การตั้งค่า Database, Timezone, Logging เป็นต้น
ซึ่งค่าที่เก็บในนี้จะอยู่ในรูปแบบ key — value
ซึ่งไฟล์นี้จะเป็นไฟล์แรกที่ Django เข้ามาอ่านเมื่อเริ่มการทำงานของ web server
"""

"""
Django settings for mvc_demo project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
"""
ตัวแปรที่เก็บ absolute path ไปหา Django project ของเรา 
ซึ่งโดยปกติข้อมูลส่วนนี้จะถูกเขียนอยู่ในรูปแบบของ Python script 
ที่ใช้อ้าง path มาถึงไฟล์ settings.py ตัวนี้ 
(สามารถทดลองโดยการ copy code ดังกล่าวมา save ไว้ในไฟล์ python ที่สร้างมาใหม่แล้วลองรันดูผลลัพธ์ได้)
"""
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""
ตัวแปรที่ใช้เก็บ hash text ใช้สำหรับการเข้ารหัสสิ่งต่าง ๆ ใน Django project 
เช่น session, cookies, password เป็นต้น ดังนั้นจึงไม่ควรเปลี่ยนค่านี้ 
และเก็บไว้เป็นความลับไม่ copy ไปแสดงในที่อื่น (โดยปกติค่านี้จะไม่ถูกแก้ไขหรือใช้งานอยู่แล้ว จะถูกใช้งานโดยอัตโนมัติเอง)
"""
SECRET_KEY = 'django-insecure-!mv(x0)ne(#t82c(t5+dg15w+e@)inyq*21q_mz%@&2q1ql2ei'

# SECURITY WARNING: don't run with debug turned on in production!
"""
ตัวแปรที่ใช้บอก Django ว่ารันใน mode debug หรือไม่ ซึ่งใน mode debug นี้ 
Django จะแสดง Error stack trace ทั้งหมดออกมาในหน้าจอ web browser 
เพื่อให้ developer เห็นบรรทัดที่ code error แล้วเข้าแก้ไขได้ทันที
"""
DEBUG = True

"""
ตัวแปรที่ใช้เก็บชื่อ domain name ของ web site เรา โดยจะเก็บในรูปแบบ list ของ string 
เช่น [‘www.mylibrary.com’, ‘128.199.148.2XX’] 
เหตุผลที่ต้องระบุชื่อของ host อย่างเจาะจงเพื่อนำไปสร้าง host header 
ใน HTTP request เพื่อใช้ป้องกัน Cross Site Scripting attack ที่มีการส่ง host ปลอมมาหลอก server เราได้
"""
ALLOWED_HOSTS = []


# Application definition
"""
ตัวแปรที่ใช้เก็บ Django Application ทั้งหมดที่ project นี้จะรู้จัก 
ซึ่งโดย default Django จะ add default Django Application บางตัวเข้ามาอยู่แล้ว
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'book',
]

"""

"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mvc_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mvc_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
