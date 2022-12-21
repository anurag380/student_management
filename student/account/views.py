from django.shortcuts import render,redirect
from . models import Course,Contact,Staff
from django.contrib import messages

# Create your views here.
def mhome(request):
    return render(request,'mainhome.html')

def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses)

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    if request.method=='POST':
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={
                'name':request.POST['name'],'out':1
            }
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')

def signin(request):
    if request.method == 'POST':
        print(request.POST['password'])
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno
            return redirect('home')
        except Staff.DoesNotExist:
            messages.error(request,'Invalid username and password')
            return redirect('signin')
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phno=request.POST['phno']
        password2=request.POST['password2']
        if password == password2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,"Email already taken")
                return redirect('signup')
            else:
                customer = Staff.objects.create(email=email,name=name,password=password,phno=phno)
                customer.save()
                messages.info(request,"User created")
                return redirect('signin')
        else: 
            messages.info(request,"Passwod is not match") 
            return redirect('signup')
    else:
        return render(request,'signup.html')

def forgot(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['password']
        if Staff.objects.filter(email=email1).exists():
            Staff.objects.filter(email=email1).update(password=password1)
            return render(request,'signin.html')
        else:
            messages.error(request,"INVALID EMAIL-ID")
            return redirect('forgot')
    return render(request,'forgot.html')

