from django.shortcuts import render,redirect
from .models import Userdata,Userdata2,PatientDetails,Alogin
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def login_page(request):
    if request.method == "POST":
        mail=request.POST.get('email')
        password=request.POST.get('password')
        user=Userdata.objects.filter(email=mail,password=password)
        if user.exists():
            return redirect('/home/')
        else:
            messages.error(request,"email and password are incorrect ")
    return render(request,'login.html')

def signup_page(request):
    if request.method =="POST":
        mail=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        user=Userdata.objects.filter(email=mail)
        if user.exists():
            messages.error(request,"user already exist")
        elif password!=confirmpassword:
            messages.info(request,"notmatch")
        else:
            Userdata.objects.create(email=mail,password=password)
            return render(request,'login.html')
    return render(request,'signup.html')

def home_page(request):
    doctors=Userdata2.objects.all()
    return render(request,'home.html',{'doctor_info':doctors})

def register_page(request):
    if request.method=="POST":
        doctorname=request.POST.get('doctorname')
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        date=request.POST.get('date')
        problem=request.POST.get('problem')
        PatientDetails.objects.create(doc_name=doctorname,patient_name=name,age=age,gender=gender,contact=contact,date=date,problem=problem)
        return render(request,'success.html')
    return render(request,'register.html')


def form(request,id):
    doctors=Userdata2.objects.get(id=id)
    return render(request,'register.html',{'doctor':doctors})

def slot_page(request):
    info=PatientDetails.objects.all()
    return render(request,'slot.html',{'information':info})

def Alogin_page(request):
    if request.method == "POST":
        mail=request.POST.get('email')
        password=request.POST.get('password')
        user=Alogin.objects.filter(email=mail,password=password)
        if user.exists():
            return redirect('/slot/')
        else:
            messages.error(request,"email and password are incorrect ")
    return render(request,'Alogin.html')