from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Course, Grade, Student
from .serializers import CourseSerializer, GradeSerializer, StudentSerializer


class LargeResultsSetPagination(LimitOffsetPagination):
    default_limit = 500


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LargeResultsSetPagination
