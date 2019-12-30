from django.core.management.base import BaseCommand
from store_api.models import store
from datetime import datetime, timedelta

class Command(BaseCommand):
    help='activating ttl'

    def handle(self, *args, **kwargs):
        items= store.objects.filter(time__lt=datetime.now()-timedelta(seconds=300))
        items.delete()

