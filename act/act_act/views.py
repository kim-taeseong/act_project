from django.shortcuts import render
from rest_framework import generics
from .models import Works
from .serializers import WorksSerializer

# Create your views here.

class WorksList(generics.ListCreateAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer