from django.db import models

class USer(models.Model):
  name=models.CharField(max_length=200)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=200)
  
  def __str__(self):
    return self.name
  
class Courses(models.Model):
  courses=models.CharField(max_length=220)
  fees=models.IntegerField()
  duration=models.CharField(max_length=50)   
  
  def __str__(self):    # for define string type 
    return self.courses
  
class Student (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile = models.IntegerField(default=0)
    college=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    course=models.ForeignKey( Courses,on_delete=models.CASCADE)
    address=models.TextField()
    image=models.FileField(upload_to='student/',max_length=100)
    
    
    def __str__(self):
       return self.name