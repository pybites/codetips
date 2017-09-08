from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Tip

class UserSerializer(serializers.ModelSerializer):
    tips = serializers.PrimaryKeyRelatedField(many=True, queryset=Tip.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tips')


class TipSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tip
        fields = ('language', 'tip', 'owner')
