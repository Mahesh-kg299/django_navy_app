from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import AircraftCarrierClass, AircraftCarrier, Armament, ACClassArmament, Builder


class ACClassArmamentSerializer(ModelSerializer):
    class Meta:
        model = ACClassArmament
        fields = ['class_id', 'quantity', 'arm_id']

class AircraftCarrierSerializer(ModelSerializer):
    vessel_class = SlugRelatedField(queryset = AircraftCarrierClass.objects.all(), slug_field='name')
    class Meta:
        model = AircraftCarrier
        fields = ['hull_number', 'name', 'vessel_class']

class AircraftCarrierClassSerializer(ModelSerializer):
    vessels = AircraftCarrierSerializer(read_only=True, many=True)
    armament = ACClassArmamentSerializer(read_only=True, many=True)
    class Meta:
        model = AircraftCarrierClass
        fields = ['class_id', 'name', 'displacement', 'length', 'beam', 'aircrafts', 'vessels', 'armament', 'builder']



class ArmamentSerializer(ModelSerializer):
    class Meta:
        model = Armament
        fields = ['arm_id', 'name', 'arm_type']

class BuilderSerializer(ModelSerializer):
    class Meta:
        model = Builder
        fields = ['builder_id', 'name']