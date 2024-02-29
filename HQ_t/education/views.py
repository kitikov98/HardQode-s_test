from django.shortcuts import render
from rest_framework import viewsets

from .models import Lesson, Product
from .serializers import ProductSerializer, LessonSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
# Create your views here.
