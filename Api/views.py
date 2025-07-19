from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import AircraftCarrierClass, AircraftCarrier, Armament, ACClassArmament, Builder
from .serializers import AircraftCarrierClassSerializer, AircraftCarrierSerializer, ArmamentSerializer, ACClassArmamentSerializer, BuilderSerializer
from django.views import View
from django.http import HttpResponse


class AircraftCarrierClassListView(ListCreateAPIView):
    queryset = AircraftCarrierClass.objects.all()
    serializer_class= AircraftCarrierClassSerializer

class AircraftCarrierListView(ListCreateAPIView):
    queryset = AircraftCarrier.objects.all()
    serializer_class = AircraftCarrierSerializer

class ArmamentListView(ListCreateAPIView):
    queryset = Armament.objects.all()
    serializer_class = ArmamentSerializer

class ACClassArmamentListView(ListCreateAPIView):
    queryset = ACClassArmament.objects.all()
    serializer_class = ACClassArmamentSerializer

class ArmamentDetailView(RetrieveAPIView):
    queryset = Armament
    serializer_class = ArmamentSerializer

class ACClassArmamentDetailView(RetrieveAPIView):
    queryset = ACClassArmament.objects.all()
    serializer_class = ACClassArmamentSerializer

class BuilderListView(ListCreateAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer