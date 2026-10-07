from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from booking_v2.serializers import signUpserializer,Appointmentserializer
from bookings.models import Appointment

from datetime import time,datetime,timedelta
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


class AppointmentListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        qs=Appointment.objects.all()

        serializer_inst =Appointmentserializer(qs,many=True)

        return Response (data=serializer_inst.data)

    def post(self,request):

        form_data = request.data

        serializer_inst =Appointmentserializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            doctor_id =cleaned_data.get("doctor")

            appointment_date =cleaned_data.get("appointment_date")

            last_appointment_object =Appointment.objects.filter(doctor=doctor_id,appointment_date=appointment_date).last()

            appointment_time =time(10,0)

            if last_appointment_object:

                cleaned_data["token_number"]=last_appointment_object.token_number+1

                next_appointment_date_time =datetime.combine(appointment_date,last_appointment_object.appointment_time)+timedelta(minutes=15)

                appointment_time =next_appointment_date_time.time()


            else:

                cleaned_data["token_number"]=1


            qs =Appointment.objects.create(**cleaned_data,appointment_time=appointment_time)

            serializer_inst=Appointmentserializer(qs)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)


class AppointmentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    # def get(self,request,pk=None):

    #     qs =Appointment.objects.get(id=pk)

    #     serializer_inst =Appointmentserializer(qs)

    #     return Response(data=serializer_inst.data)
    serializer_class =Appointmentserializer

    queryset =Appointment.objects.all()


    

    
            


            
