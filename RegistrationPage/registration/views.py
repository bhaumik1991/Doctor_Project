from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Doctor, Prescription
from django.http import HttpResponseRedirect
import xhtml2pdf.pisa as pisa
from io import BytesIO
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    if request.method == "POST":
        if (request.POST.get('full_name') and request.POST.get('hospital_name') and request.POST.get('email')
            and request.POST.get('password') and request.POST.get('address') and request.POST.get('zip_code')
            and request.POST.get('dob') and request.POST.get('gender') and  request.POST.get('phone_number')):
            doctor = Doctor()
            doctor.full_name = request.POST.get('full_name')
            doctor.hospital_name = request.POST.get('hospital_name')
            doctor.email = request.POST.get('email')
            doctor.password = request.POST.get('password')
            doctor.address = request.POST.get('address')
            doctor.zip_code = request.POST.get('zip_code')
            doctor.dob = request.POST.get('dob')
            doctor.gender = request.POST.get('gender')
            doctor.phone_number = request.POST.get('phone_number')
            doctor.save()
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html' )
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        print ("Email",email)
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HttpResponseRedirect('/%s/' % email)
            else:
                print("Invalid User!")
        else:
            print("Invalid login")



    return render(request, 'welcome1.html')

def prescription(request):
    if request.method == "POST":
        data = Doctor.objects.get(pk=1)
        context = {'object':data}
        return render(request, 'welcome1.html',context)
    else:
        # form = loginform
        return render(request, 'login.html')

def prescription_create(request):
    if request.method == "POST":
        if (request.POST.get('patient_name') and request.POST.get('phone_number1') and request.POST.get('age')
            and request.POST.get('weight') and request.POST.get('gender') and request.POST.get('type')
            and request.POST.get('mediciene_name') and request.POST.get('mediciene_power') and  request.POST.get('does')
            and request.POST.get('day') and request.POST.get('comments')):
            prescription = Prescription()
            prescription.patient_name = request.POST.get('patient_name')
            prescription.phone_number1 = request.POST.get('phone_number1')
            prescription.age = request.POST.get('age')
            prescription.weight = request.POST.get('weight')
            prescription.gender = request.POST.get('gender')
            prescription.type = request.POST.get('type')
            prescription.mediciene_name = request.POST.get('mediciene_name')
            prescription.mediciene_power = request.POST.get('mediciene_power')
            prescription.dose = request.POST.get('dose')
            prescription.day = request.POST.get('day')
            prescription.comments = request.POST.get('comments')
            prescription.save()
        return render(request, 'preview.html')
    else:
        return render(request, 'welcome1.html')
def show_prescription(request):
    data = Prescription.objects.get(pk=1)
    data1 = Doctor.objects.get(pk=1)
    context  = {'prescription':data, 'object':data1}
    return render(request,'prescription.html',context)

def Logout(request):
    
    return render(request,'login.html')
