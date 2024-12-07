from rest_framework import serializers
from .models import ClaimFile, Claim

class ClaimFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClaimFile
        fields = ['id', 'claim', 'file', 'description']

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = ['id', 'name', 'sender_federation', 'receiver_federation', 'start_time',
                  'end_time', 'place', 'format', 'status', 'contest_type', 'contest_char',
                  'contest_discipline', 'contest_age_group']
        
        def create(self, validated_data):
            claim = Claim.objects.create(
                name=validated_data['name'],
                sender_federation=validated_data['sender_federation'],
                receiver_federation=validated_data['receiver_federation'],
                start_time=validated_data['start_time'],
                end_time=validated_data['end_time'],
                place=validated_data['place'],
                format=validated_data['format'],
                status=validated_data['status'],
                contest_type=validated_data['contest_type'],
                contest_char=validated_data['contest_char'],
                contest_discipline=validated_data['contest_discipline'],
                contest_age_group=validated_data['contest_age_group'],
            )
            return claim