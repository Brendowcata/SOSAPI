from dataclasses import fields
from pyexpat import model
from threading import local
from rest_framework import serializers
from endereco.serializers import EnderecoSerializer
from local.models import Local 

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('tipo', 'titulo', 'numero', 'endereco',)

class LocalSerializerRetrieve(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = local
        fields = ('tipo', 'titulo', 'numero', 'endereco',)