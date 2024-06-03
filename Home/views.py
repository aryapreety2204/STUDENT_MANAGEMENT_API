from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

# Create your views here.
def index(request):
    
     return render(request, 'index.html')
     
def signup(request):
     return render(request,'sign-up.html')

def courses(request):
      user=Courses.objects.all()
      return render(request,'courses.html' ,{"user":user})

def dashboard(request):
     return render(request,'dashboard.html')

def profile(request):
     return render(request,"profile.html")

def viewstudents(request):  
     course_obj=Courses.objects.all()
     student_obj=Student.objects.all()
     return render(request,'viewstudents.html',{ 'course_obj':course_obj ,'student_obj':student_obj})

def sign_in(request):
    if request.method=='POST':
        email=request.POST.get('email')
        user_password=request.POST.get('password')
        if USer.objects.filter(email=email).exists():
            obj=USer.objects.get(email=email)
            password=obj.password
            if check_password(user_password,password):
                return redirect('/profile/')
            else:
                messages.error( request, "Password incorrect ")
                return redirect('/')
        else:
             messages.error( request , "Email not registered")
             return redirect('/')
     
   

def create_user(request):
    if request.method=="POST":
        name = request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if USer.objects.filter(email=email).exists():
            return HttpResponse("Already Exist")
        else:
            USer.objects.create(name=name,email=email,password=password)
            return redirect("/")
      
      
def add_courses(request):
       if request.method == "POST":
          courses=request.POST['courses']
          fees = request.POST['fees']
          duration= request.POST['duration']
          if Courses.objects.filter(courses=courses).exists():
               return HttpResponse("course Already Added")
          else:
               Courses.objects.create(courses=courses, fees=fees,duration=duration)
               return redirect("/courses/")

               
def delete_course(request , pk):
     dt = Courses.objects.get(id=pk)
     dt.delete()
     return redirect('/courses/')

def update(request,uid):
    user_obj = Courses.objects.get(id=uid)
    return render(request,"update_courses.html",{"user_obj":user_obj})

def update_course_view(request):
     if request.method == "POST":
          uid = request.POST['uid']
          courses = request.POST['courses']
          fees = request.POST['fees']
          duration = request.POST['duration']
          Courses.objects.filter(id=uid).update(courses=courses , fees=fees, duration=duration)
          return redirect("/courses/")
     
     
def add_student(request):
    if request.method=="POST" :
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        college= request.POST['college']
        address =request.POST['address']
        degree=request.POST['degree']
        course_id=request.POST['courses']
        new_course=Courses.objects.get(id=course_id)
        image=request.FILES.get('image')
        if Student.objects.filter(email=email).exists():
            return HttpResponse('Student already exists!')
        else:
            Student.objects.create(name=name,email=email,mobile=mobile,college=college, address=address,degree=degree, course=new_course,image=image)
            return redirect("/viewstudents/")
          
                    
            
          