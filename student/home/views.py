from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from account.models import Staff,Contact
from . forms import StudentsForm,Students

# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Staffs(View):
    def get(self,request):
        customer=Staff.objects.all()
        return render(request,'staff.html',{'customer':customer})

class Student(View):
    def get(self,request):
        stu=Students.objects.all()
        return render(request,'student.html',{'form':stu})
        
class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'enquiry.html',{'form':customer})
        
class Editprofile(View):
    def get(self,request):
        # print(request.GET['edit'])
        edit1=request.GET['edit']
        edit=Students.objects.filter(student_id=edit1)
        return render(request,'editprofile.html',{'forms':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Students.objects.filter(student_id=edit1).exists():
                if request.POST['student_address']:
                    Students.objects.filter(student_id=edit1).update(student_address=request.POST['student_address'])
                if request.POST['student_place']:
                    Students.objects.filter(student_id=edit1).update(student_place=request.POST['student_place'])
                if request.POST['student_name']:
                    Students.objects.filter(student_id=edit1).update(student_name=request.POST['student_name'])
                if request.POST['student_email']:
                    Students.objects.filter(student_id=edit1).update(student_email=request.POST['student_email'])
                if request.POST['student_phone']:
                    Students.objects.filter(student_id=edit1).update(student_phone=request.POST['student_phone'])
                student=Students.objects.all()
                return render(request,'student.html',{'form':student})


class Profile(View):
    def get(self,request):
        print(12)
        if request.session['email'] is not None:
         customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'form':customer})


class Form(View):
    def get(self,request):
        form=StudentsForm()
        return render(request,'form.html',{'form':form})
    def post(self,request):
        if request.method=='POST':
            form=StudentsForm(request.POST)
            if form.is_valid():
                form.save()
                stu=Students.objects.all()
                return render(request,"student.html",{'form':stu})
            else:
                print("Form is not Valid")
            return redirect("show")

class Edit(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render(request,'edit.html',{'form':edit})
    def post(self,request):
        edit1=request.session['email']
        # print(1)
        if request.method == 'POST':
            # print(2)
            if Staff.objects.filter(email=edit1).exists():
                # print(3)
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Staff.objects.filter(email=request.POST['email']).exists():
                            print(request.POST['email'])
                            edit=Staff.objects.filter(email=edit1)
                            messages.error(request,"EMAIL IS ALREADY EXISTS")
                            return render(request,'edit.html',{'form':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Staff.objects.filter(email=request.session['email'])
                return render(request,'profile.html',{'form':customer})



class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        Students.objects.filter(student_id=delete).delete()
        student=Students.objects.all()
        return render(request,'student.html',{'form':student})

