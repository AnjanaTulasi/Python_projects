from django.http import HttpResponse
from django.shortcuts import render, redirect
from .admin import PatientsLogin, DoctorsLogin
from .models import AppointmentData,AcceptAppointment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 
def mainPage(request):
    if request.method == 'GET':
        return render(request, 'mainpage.html')
    else:
        # Fetch credentials from POST request  
        username_patient = request.POST.get('username')
        password_patient = request.POST.get('password')
        username_doctor = request.POST.get('user')
        password_doctor = request.POST.get('pass')

        # Authenticate patient user
        patient_user = authenticate(request, username=username_patient, password=password_patient)

        # Authenticate doctor user
        doctor_user = authenticate(request, username=username_doctor, password=password_doctor)

        # Determine user type and redirect
        if patient_user is not None:
            login(request, patient_user)
            return redirect(request,'patientslogin.html')
        elif doctor_user is not None:
            login(request, doctor_user)
            return redirect(request,'doctorslogin.html')
        else:
            # Authentication failed; stay on the main page with an error
            return render(request, 'mainpage.html', {'error': 'Invalid credentials'})

def patients_login(request):
    return render(request, 'patientslogin.html')

def doctors_login(request):
    return render(request, 'doctorslogin.html')

def take_appointment(request):
    if request.method == 'GET':
        data = AppointmentData.objects.all()
        return render(request, 'takeappointment.html',{'data':data})
    else:
        patients_name1 = request.POST['patients_name']
        age1 = request.POST['age']
        gender1 = request.POST['gender']
        mobile1 = request.POST['mobile']
        blood_group1 = request.POST['blood_group']
        doctors_name1 = request.POST['doctors_name']
        location1 = request.POST['location']
        problem1 = request.POST['problem']
        AppointmentData.objects.create(
            patients_name = patients_name1,
            age = age1,
            gender = gender1,
            mobile = mobile1,
            blood_group = blood_group1,
            doctors_name = doctors_name1,
            location = location1,
            problem = problem1,
        ).save()
        data = AppointmentData.objects.all()
        return render(request, 'takeappointment.html',{'data':data})

def check_status(request):
    data = AcceptAppointment.objects.all()
    return render(request, 'checkstatus.html',{'data':data})

def my_history(request):
    data = AcceptAppointment.objects.all()
    return render(request, 'myhistory.html')





def doctor_details(request):
    return render(request, 'doctordetails.html')
def check_appointment(request):
    data = AppointmentData.objects.all()
    return render(request, 'checkappointment.html',{'data':data})
def acceptPage(request):
    if request.method == 'GET':
        data = AcceptAppointment.objects.all()
        return render(request, 'acceptappointment.html',{'data':data})
    else:
        date1 = request.POST['date']
        time1 = request.POST['time']
        day1 = request.POST['day']
        AcceptAppointment(
            date = date1,
            time = time1,
            day = day1
        ).save()
        data = AcceptAppointment.objects.all()
        return render(request, 'acceptappointment.html',{'data':data})

def logoutpage(request):
    logout(request)
    return HttpResponse('logout here!!!')
