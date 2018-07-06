from django.contrib.auth.models import User, Group # import models to serializers
from rest_framework import serializers

#

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User # Here We Define the model
        fields = ('username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name')
