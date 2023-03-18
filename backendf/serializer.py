from rest_framework import serializers

class RegisterSerial(serializers.Serializer):
    Email = serializers.CharField()
    city = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField()


class meetingsSerial(serializers.Serializer):
    name = serializers.CharField() 
    patient=serializers.CharField()
    sent=serializers.CharField()
    category=serializers.CharField()
    slot=serializers.CharField()
    report = serializers.CharField()

class passwordSerial(serializers.Serializer):
    Email = serializers.CharField()
    password = serializers.CharField()

class serviceSerial(serializers.Serializer):
    service = serializers.CharField()
    image = serializers.CharField()


class doctorserial(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    place = serializers.CharField()
    password = serializers.CharField()



class deletedoctorserial(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    

class deleteslot(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()

class delcat(serializers.Serializer):
    service = serializers.CharField()