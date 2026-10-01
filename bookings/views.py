from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer



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

            last_appointment_object =Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()

            if last_appointment_object:

                new_token =last_appointment_object.token +1

            else:

                new_token =1

                
                return Response(data={"token":new_token,"status":"booked"})

        else:

            return Response (data=serializer_inst.errors)

           

            
        
