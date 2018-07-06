from django.contrib.auth.models import User
from rest_framework import serializers
from pastebin.models import Snippet

class NameUserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name')


class SnippetModelSerializer(serializers.ModelSerializer):

    user = NameUserSerializer()
    full_name = serializers.SerializerMethodField()
    created_count = serializers.SerializerMethodField()

    #Campos que llevara el resultado de la serializacion
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'lang', 'user', 'full_name', 'created_count')

    #define el campo que quieres traer de la tabla relacionada
    def get_full_name(self, obj):
        return obj.user.get_full_name()

    #Cuenta cuantos existen
    def get_created_count(self, obj):
        return obj.user.snippet_set.count()