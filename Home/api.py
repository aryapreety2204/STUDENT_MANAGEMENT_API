from .models import*
from.serializers import USerSerializers
from.serializers import CoursesSerializers
from.serializers import StudentSerializers
from rest_framework import generics


class CreateUSerApi(generics.CreateAPIView):
  queryset = USer.objects.all()
  serializer_class = USerSerializers

  
# class UpdateUSerApi(generics.UpdateAPIView):
#   queryset = USer.objects.all()
#   serializer_class = USerSerializers

class itemList(generics.ListAPIView):
  queryset = USer.objects.all()
  serializer_class = USerSerializers
  

class CreateCourseApi(generics.ListAPIView):
  queryset = Courses.objects.all()
  serializer_class = CoursesSerializers
  
class CreateStudentApi(generics.ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers
  
class CourseUpdateApi(generics.RetrieveUpdateAPIView):
  queryset = Courses.objects.all()
  serializer_class = CoursesSerializers
  
  
class CourseDeleteApi(generics.DestroyAPIView):
  queryset = Courses.objects.all()
  serializer_class = CoursesSerializers
  
class StudentUpdateApi(generics.RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers
  
  
class StudentDeleteApi(generics.DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers