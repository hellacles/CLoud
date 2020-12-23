from rest_framework import serializers
from .models import VoiceTrain

class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceTrain
        fields = ('id', 'user', 'voice')