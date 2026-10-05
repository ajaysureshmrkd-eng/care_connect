from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from booking_v2.serializers import signUpserializer

class signUpView(APIView):

    def post (self,request):

        form_data =request.data

        serializer_inst =signUpserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data=serializer_inst.validated_data

            user_object=User.objects.create_user(**cleaned_data)

            serializer_inst =signUpserializer(user_object)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

