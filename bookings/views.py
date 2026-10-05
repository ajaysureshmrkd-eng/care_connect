from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer
from staff.models import Doctor


class AppointmentListCreateView(APIView):

    def get(self,request):

        qs =Appointment.objects.all()

        serializer_inst =AppointmentSerializer(qs,many=True)

        return Response(data=serializer_inst.data)

    def post(self,request):

        form_data =request.data

        serializer_inst =AppointmentSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            doctor =cleaned_data.get("doctor")

            appointment_date =cleaned_data.get("appointment_date")

            new_token =0

            last_appointment_object =Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()

            if last_appointment_object:


                new_token =last_appointment_object.token_number +1

            else:

                new_token =1

            doctor_object =Doctor.objects.get(id =doctor)

            cleaned_data =[doctor]=doctor_object

            Appointment.objects.create(**cleaned_data,token_number=new_token)

            respones_data ={
                "status":"booked",
                "token":new_token
            }

            return Response (data=respones_data)

        else:

            return Response (data=serializer_inst.errors)

                

           

            
        
