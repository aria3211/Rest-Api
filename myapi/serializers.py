from rest_framework import serializers
from .models import Hero , Peple


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name','alies')

class PepleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peple
        fileds = ('name','age')

