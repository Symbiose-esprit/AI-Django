from rest_framework import serializers
from .models import diseaseinfo


class diseaseinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = diseaseinfo
        fields = [ "diseasename", "confidence"]
