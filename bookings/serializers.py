from rest_framework import serializers

from datetime import datetime

class AppointmentSerializer(serializers.Serializer):

    patient_name =serializers.CharField()

    phone=serializers.CharField()
    
    doctor=serializers.IntegerField()

    appointment_date =serializers.DateField()

    token_number =serializers.DateField(read_only =True)

    appointment_time =serializers.TimeField(read_only=True)

    problem =serializers.CharField()

    created_at =serializers.DateTimeField(read_only=True)

    def validate(self, validate_data):

        appointment_date =validate_data.get("appointment_date")

        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("invalid error")

        return validate_data
        





