from django.shortcuts import render
from meeting import task
from .serializers import MeetingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import Meeting

# Create your views here.



class MeetingViewset(generics.GenericAPIView):
    serializer_class = MeetingSerializer



    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        meeting = serializer.save()
        return Response({
            "meting": MeetingSerializer(meeting,context=self.get_serializer_context()).data,
            "message": "meeting created Succesfully"
        })