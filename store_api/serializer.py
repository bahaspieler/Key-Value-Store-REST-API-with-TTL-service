from rest_framework.serializers import ModelSerializer
from .models import store

class StoreSerializer(ModelSerializer):
    class Meta:
        model = store
        fields = ['pk', 'key', 'value']



