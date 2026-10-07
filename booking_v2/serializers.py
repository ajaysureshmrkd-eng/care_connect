from rest_framework import serializers
from bookings.models import Appointment

from django.contrib.auth.models import User

from datetime import datetime


class signUpserializer(serializers.ModelSerializer):


    class Meta:

        model =User

        fields=["username","email","password"]

class Appointmentserializer(serializers.ModelSerializer):

    doctor =serializers.StringRelatedField()

    class Meta:

        model =Appointment

        fields ="__all__"

        read_only_fields =["id","token_number","appointment_time","created_at"]


    def validate(self, validated_data):

        appointment_date =validated_data.get("appointment_date")

        doctor =validated_data.get("doctor")

        phone =validated_data.get("phone")

        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("invalid date,date should be current date")

        last_appointment_object =Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()

        if last_appointment_object:

            if last_appointment_object.token_number ==25:

                raise serializers.ValidationError("booked slot full")


        appointment_phone =Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date,phone=phone)

        if appointment_phone:

            raise serializers.ValidationError("already booked......")

        return validated_data
        
        






