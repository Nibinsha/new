from django.shortcuts import render
from .forms import *
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def login(request):
    loginform = LoginForm()
    Registrationform = RegistrationForm()
    return render(request, 'login.html', {'loginform':loginform,'Registrationform':Registrationform})


@csrf_exempt
def registration(request):
    if request.method == "POST":
        a = request.body.decode('utf-8')
        body = json.loads(a)
        post = User()
        post.firstName = body['firstName']
        post.contactNo = body['contactNo']
        post.email = body['email']
        password = body['password']
        post.password = make_password(password)
        post.save()
    return JsonResponse({'status': "success"})


@csrf_exempt
def loggedin(request):
    if request.method == "POST":
        a = request.body.decode('utf-8')
        body = json.loads(a)
        email = body['email'].lower()
        password = body['pswd']
        if email and password:
            user = User.objects.get(email=email)
            if user is not None:
                if check_password(password, user.password):
                    return JsonResponse({'status': "success"})
            return JsonResponse({'status': "wrong credentials"})
        else:
            return JsonResponse({'status': "wrong credentials"})
    loginform = LoginForm()
    Registrationform = RegistrationForm()
    return render(request, 'login.html', {'loginform': loginform, 'Registrationform': Registrationform})

def index(request):
    leaveform = LeaveForm()
    return render(request, 'index.html',{'leaveform':leaveform})

@csrf_exempt
def leaveSave(request):
    if request.method == "POST":
        a = request.body.decode('utf-8')
        body = json.loads(a)
        post = Leave()
        post.desc = body['desc']
        post.user = User.objects.get(userId=body['user'])
        post.date = body['date']
        post.save()
    return JsonResponse({'status': "success"})

@csrf_exempt
def fetchleaveData(request):
    lvs = Leave.objects.all().values('desc','user__firstName','date','leaveId')
    lveEditform = LeaveEditForm()
    return render(request, 'lve.html', {'lvs': list(lvs),'lveEditform':lveEditform})


@csrf_exempt
def fetchParticularLveData(request):
    a = request.body.decode('utf-8')
    body = json.loads(a)
    lvedata = Leave.objects.filter(leaveId=body['id']).values('desc','user__firstName','date','leaveId')
    return JsonResponse({'status': "success",'lve': list(lvedata)})


@csrf_exempt
def SavefetchParticularLveData(request):
    if request.method == "POST":
        a = request.body.decode('utf-8')
        body = json.loads(a)
        post = Leave.objects.get(leaveId=body['lveId'])
        post.desc = body['desc']
        post.date = body['date']
        post.save()
    return JsonResponse({'status': "success"})