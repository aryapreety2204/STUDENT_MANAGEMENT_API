from rest_framework import serializers
from.models import*


class USerSerializers(serializers.ModelSerializer):
  class Meta:
    model = USer
    fields = '__all__'

class CoursesSerializers(serializers.ModelSerializer):
  class Meta:
    model = Courses
    fields = '__all__'
    

class StudentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Student 
    fields = '__all__'
 
      





    


     
 
  
