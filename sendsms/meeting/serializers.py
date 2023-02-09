from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
   class Meta:
      model = Meeting
      fields = '__all__'


   def create(self, validated_data):
      meeting = Meeting(
         phone_number = validated_data['phone_number'],
         date_time = validated_data['date_time']
      )
      meeting.save()
      return meeting