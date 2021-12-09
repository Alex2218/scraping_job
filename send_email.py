import os, sys
import django
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'job_ua.settings'

django.setup()