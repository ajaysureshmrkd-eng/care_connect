from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializer

# Create your views here.

class DoctorListCreateView(APIView):


    authentication_classes =[authentication.BasicAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def get(self,request):

        qs =Doctor.objects.all()

        serializer_inst =DoctorSerializer(qs,many=True)

        return Response(data=serializer_inst.data)

    def post(self,request):

        form_data =request.data

        serializer_inst =DoctorSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            Doctor.objects.create(**cleaned_data)

            return Response(data=serializer_inst.validated_data)

        else:

            return Response(data=serializer_inst.errors)



class DoctorRetrieveUpdateDeleteView(APIView):

    def get (self,request,pk=None):

        qs =Doctor.objects.get(id=pk)

        serializer_inst =DoctorSerializer(qs)

        return Response (data=serializer_inst.data)

    def put(self,request,pk=None):

         form_data =request.data

         serializer_inst =DoctorSerializer(data=form_data)

         if serializer_inst.is_valid():

              cleaned_data =serializer_inst.validated_data

              Doctor.objects.filter(id=pk).update(**cleaned_data)

              return Response (data=serializer_inst.validated_data)

         else:

              return Response (data=serializer_inst.errors)
         


    def delete(self,request,pk=None):
    
            qs =Doctor.objects.filter(id=pk).delete()
    
            return Response (data={"message":"deleted"})



class UserAdminCreateView(APIView):

     def post(self,request):

          form_data =request.data

          serializer_inst =UserSerializer(data=form_data)

          if serializer_inst.is_valid():

               cleaned_data =serializer_inst.validated_data

               User.objects.create_superuser(**cleaned_data)
                
               return Response (data=serializer_inst.data)

          else:

               return Response (data=serializer_inst.errors)

    




