from django.shortcuts import render
from rest_framework import viewsets
from .models import Jobs
from .serializers import JobSerializer

class ListJobView(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

# Create your views here.
