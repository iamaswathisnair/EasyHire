from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from . models import reg,Jobposting,Gallery,workerreg1,Complaints,Feedback,Workerbooking
import smtplib
# Create your views here.
def index(request):
    return render(request,'index.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    subject_template_name = 'password_reset_subject.txt'
    email_template_name = 'password_reset_email.html'
    success_url = '/password_reset/done/'

def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def home1(request):
   return render(request,'home.html')

def search(request):
   return render(request,'search.html')

def reg1(request):
    if request.method =='POST':
      fname = request.POST.get('rfname')
      lname = request.POST.get('rlname')
      address1 = request.POST.get('raddress')
    #   phone = request.POST.get('rcontact')
      num = request.POST.get('rcontactno')
      mail = request.POST.get('Email')
      passw = request.POST.get('rpass')
      reg(firstname=fname,lastname=lname,address=address1,contactno=num,email=mail,password=passw).save()
      return render(request,'home.html')
    else:
       return render(request,'reg.html')
def login(request):
   if request.method=='POST':
      mail= request.POST.get('Email')
      passw = request.POST.get('rpass')
      confirm_passw = request.POST.get('confirm_rpass')

      if passw != confirm_passw:
            msge = 'Password and Confirm Password do not match'
            return render(request, 'login.html', {'me': msge})
      

      cr = reg.objects.filter(email=mail,password=passw)
      if cr:
         details = reg.objects.get(email= mail, password = passw)
         Email = details.email
         name=details.firstname
         request.session['cs']=Email
         request.session['name']=name

         return render(request,'home.html')
      else :
            if not reg.objects.filter(email=mail).exists():
                msge='your email is incorrect'
                return render(request,'login.html',{'me':msge})     
            else:
                msge='your password is incorrect'
                return render(request,'login.html',{'me':msge})
   else:
         return render(request,'login.html')




def workerreg(request):
    if request.method =='POST':
      fname = request.POST.get('rfname')
      lname = request.POST.get('rlname')
      job = request.POST.get('rjob')
      quilification1 = request.POST.get('rquilificaion')
      address1 = request.POST.get('raddress')
    #   phone = request.POST.get('rcontact')
      num = request.POST.get('rcontactno')
      imgg=request.FILES['image']
      mail = request.POST.get('Email')
      passw = request.POST.get('rpass')
      workerreg1(firstname=fname,lastname=lname,imgg=imgg,job=job,quilification=quilification1,address=address1,contactno=num,email=mail,password=passw).save()
    return render(request,'workreg.html')
    
def workerlogin(request):
   if request.method=='POST':
      mail= request.POST.get('Email')
      print(mail)
      passw = request.POST.get('rpass')
      cr =  workerreg1.objects.filter(email=mail,password=passw)
      if cr:
         details = workerreg1.objects.get(email= mail, password = passw)
         Email = details.email
         name= details.firstname
         request.session['cs']=Email
         request.session['worker']=name

         return render(request,'workerhome.html')
      else :
            if not workerreg1.objects.filter(email=mail).exists():
                msge='your email is incorrect'
                return render(request,'login.html',{'me':msge})     
            else:
                msge='your password is incorrect'
                return render(request,'login.html',{'me':msge})
   else:
         return render(request,'workerlogin.html')


def joblisting(request):
   varii=request.session['cs']
   cr=Jobposting.objects.filter(email=varii)
   print(cr) 
   return render(request,'joblisting.html',{'data':cr})


def deleteee(request,id):
    data=Jobposting.objects.get(id=id)
    data.delete()
    return render(request,'workerhome.html')


def jobposting(request):
   s=request.session['cs']
   cr=workerreg1.objects.get(email=s)
   n=cr.firstname
   e=cr.email
   if request.method =='POST':
      jname = request.POST.get('rjname')
      location = request.POST.get('rlocation')
      category=request.POST.get('category')
      email = request.POST.get('remail')
      username = request.POST.get('runame')
      dailywages = request.POST.get('rwages')
      description = request.POST.get('rdescription')
      Jobposting(jobname=jname,category=category,location=location,email=email,username=username,dailywages=dailywages,description=description).save()
      return render(request,'workerhome.html')
   else:
      return render(request,'jobposting.html',{"sf":n,'ef':e})




def workerhome(request):
   return render(request,'workerhome.html')     
    
def choice(request):
   return render(request,'choice.html')

def loginchoice(request):
   return render(request,'loginchoice.html')

def profile1(request):
   c=request.session['cs']
   cr=reg.objects.get(email=c)
   id=cr.id
   pfname=cr.firstname
   plname=cr.lastname
   paddress=cr.address
   pcontact=cr.contactno
   pemail=cr.email
   return render(request,'profile.html',{'id':id,'fname':pfname,'lname':plname,'address':paddress,'contact':pcontact,'email':pemail})

def update(request):
   c=request.session['cs']
   cr=reg.objects.get(email=c)
   id=cr.id
   pfname=cr.firstname
   plname=cr.lastname
   paddress=cr.address
   pcontact=cr.contactno
   pemail=cr.email
   ppassword=cr.password
   return render(request,'update.html',{'id':id,'fname':pfname,'lname':plname,'address':paddress,'contact':pcontact,'email':pemail,'password':ppassword})


def updateprofile(request):
   if request.method =='POST':
      id=request.POST.get('id')
      fname = request.POST.get('rfname')
      lname = request.POST.get('rlname')
      address1 = request.POST.get('raddress')
    #   phone = request.POST.get('rcontact')
      num = request.POST.get('rcontactno')
      mail = request.POST.get('Email')
      passw = request.POST.get('rpass')
      dt=reg.objects.get(id=id)
      
      dt.firstname=fname
      dt.lastname=lname
      dt.contactno=num
      dt.address=address1
      dt.email=mail
      dt.password=passw
      dt.save()
      return render(request,'home.html')
   
def workerprofile(request):
   c=request.session['cs']
   cr=workerreg1.objects.get(email=c)
   id=cr.id
   pfname=cr.firstname
   plname=cr.lastname
   pjob=cr.job
   pqualification=cr.quilification
   paddress=cr.address
   pcontact=cr.contactno
   pemail=cr.email
   ppassword=cr.password
   return render(request,'workerupdate.html',{'id':id,'fname':pfname,'lname':plname,'job':pjob,'quilification':pqualification,'address':paddress,'contact':pcontact,'email':pemail,'password':ppassword})


def workerupdate(request):
   if request.method =='POST':
      id=request.POST.get('id')
      fname = request.POST.get('rfname')
      lname = request.POST.get('rlname')
      jobname=request.POST.get('rjob')
      quilification=request.POST.get('quilification')
      address1 = request.POST.get('raddress')
    #   phone = request.POST.get('rcontact')
      num = request.POST.get('rcontactno')
      mail = request.POST.get('Email')
      passw = request.POST.get('rpass')
      
      dt=workerreg1.objects.get(id=id)
      dt.firstname=fname
      dt.lastname=lname
      dt.job=jobname
      dt.quilification=quilification
      dt.contactno=num
      dt.address=address1
      dt.email=mail
      dt.password=passw
      dt.save()
      return render(request,'home.html')
   else:
    return render(request,'workerupdate.html')
   
def gallery(request):
   if request.method =='POST':
      workername = request.POST.get('workername')
      desc= request.POST.get('desc')
      imgg=request.FILES['imgg']
      Gallery(workername=workername,desc=desc,imgg=imgg).save()
      return render(request,'workerhome.html')
   else:
      name= request.session['worker']
      return render(request,'gallery.html',{'name':name})
       
       



def userjoblisting(request):
    category = 'others'
    jobs = Jobposting.objects.filter(category=category)
    return render(request,'userjoblisting.html',{'jobs':jobs})

def user_complaints(request):
   if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       number=request.POST.get('number')
       message=request.POST.get('message')
       Complaints(name=name,email=email,number=number,message=message).save()
       return render (request,'home.html')
      
   else:
       name=request.session['name']
       return render (request,'user_complaints.html',{'name':name})

def user_feedback(request):
   if request.method=='POST':
       name=request.POST.get('name')
       message=request.POST.get('message')
       Feedback(name=name,message=message).save()
       return render (request,'home.html')
      
   else:
       name=request.session['name']
       return render (request,'user_feedback.html',{'name':name})

def category_jobs(request,category):
    jobs = Jobposting.objects.filter(category=category)
    return render(request, 'category_jobs.html', {'jobs': jobs, 'category': category})

def search (request):  
    if request.method == 'POST':   
        job=request.POST.get('job') 
        location=request.POST.get('location')  
        da= Jobposting.objects.filter(jobname__icontains=job,location__icontains=location)
        if da:
         return render(request,'seeing.html',{'data':da})   
        else: 
            msge="Sorry no results found "          
            return render(request,'home.html',{'msge':msge})
        
    else:
            return render(request,'home.html')
       
def worker_booking(request,workername):
    
    if request.method=='POST':
        username=request.POST.get('name')
        workername=request.session['worker']
      #   workername=request.POST.get('venue')
        date=request.POST.get('date')
        requirement=request.POST.get('requirement')
      #   emaill=request.session['mysession']
        status='waiting'

      #   w_name=request.session['w_name']
        Workerbooking(username=username,date=date,requirement=requirement,workername=workername,w_status=status).save()
        return render(request,'home.html')
        
    else:
        name= request.session['name']
      #   workerrname=request.session['worker']
        return render(request,'workerbooking.html',{'name':name,'workername':workername})
    



def listworks(request,name):
   details = Gallery.objects.filter(workername=name)
   return render(request,'listgallery.html',{'details':details})


def request(request):
    workername=request.session['worker']
    data=Workerbooking.objects.filter(workername=workername)
    #d1=Jobposting.objects.filter(username=workername)
    #jobname=d1.category
    return render(request,'request.html',{'data':data})

def userbkinglist(request):
    name= request.session['name']
    data=Workerbooking.objects.filter(username=name)
    return render(request,'userbkinglist.html',{'data':data})

def deletebooking(request,id):
    data=Workerbooking.objects.get(id=id)
    name=data.username
    workername=data.workername
    cr=workerreg1.objects.get(firstname=workername)
    mail=cr.email
    data.delete()


    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
 
 
# Authentication
    s.login("nefsal003@gmail.com","htxalvzrrkxupspv")
 
# message to be sent
    message = f"sorry your booking has been cancelled by {name}!"
 
# sending the mail
    s.sendmail("nefsal003@gmail.com",mail, message)
 
# terminating the session
    s.quit()
    return render(request,'userbkinglist.html')


def update_status(request, workerbooking_id):
    if request.method == 'POST':
        new_status = request.POST.get('new_status')


        workerbooking = Workerbooking.objects.get(id=workerbooking_id)
        username=workerbooking.username


        data=reg.objects.get(firstname=username)
        email=data.email


        workerbooking.w_status = new_status
        workerbooking.save()

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()
 
 
# Authentication
        s.login("nefsal003@gmail.com","htxalvzrrkxupspv")
 
# message to be sent
        message = "Request Approved Successfully"
 
# sending the mail
        s.sendmail("nefsal003@gmail.com",email, message)
 
# terminating the session
        s.quit()
        return render(request,'request.html')
    

def book_job(request):
    
    if request.method=='POST':
        username=request.POST.get('name')
        workername=request.POST.get('workername')
      #   workername=request.POST.get('venue')
        date=request.POST.get('date')
        requirement=request.POST.get('requirement')
      #   emaill=request.session['mysession']
        status='waiting'

      #   w_name=request.session['w_name']
        Workerbooking(username=username,date=date,requirement=requirement,workername=workername,w_status=status).save()
        
        data=workerreg1.objects.get(firstname=workername)
        email=data.email


        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()
 
 
# Authentication
        s.login("nefsal003@gmail.com","htxalvzrrkxupspv")
 
# message to be sent
        message = f"You have one booking from {username}.Please check our website for more informations"
 
# sending the mail
        s.sendmail("nefsal003@gmail.com",email, message)
 
# terminating the session
        s.quit()
        
        return render(request,'home.html')
        
    else:
        name= request.session['name']
      #   workerrname=request.session['worker']
        return render(request,'workerbooking.html',{'name':name,'workername':workername})
