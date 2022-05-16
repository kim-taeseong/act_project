from rest_framework import serializers
from .models import Works

class WorksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Works
        fields = ['id', 'date', 'work', 'completed']