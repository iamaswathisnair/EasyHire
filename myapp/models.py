from django.db import models
w_choice=(('waiting','waiting'),('Request Accepted','Request Accepted'),('Request Denied','Request Denied'))


# Create your models here.
class reg(models.Model):
 firstname = models.CharField(max_length=20,null='true')
 lastname = models.CharField(max_length=20)
 contactno = models.IntegerField()
 email = models.EmailField()
 address = models.CharField(max_length=80)
 password = models.CharField(max_length=20)
 
 
class workerreg1(models.Model):
 firstname = models.CharField(max_length=20)
 lastname = models.CharField(max_length=20)
 job=models.CharField(max_length=20)
 quilification=models.CharField(max_length=50)
 contactno = models.IntegerField()
 email = models.EmailField()
 imgg=models.ImageField()
 address = models.CharField(max_length=80)
 password = models.CharField(max_length=20)

 
class Jobposting(models.Model):
     jobname=models.CharField(max_length=20)
     location=models.CharField(max_length=20)
     email=models.CharField(max_length=20)
     username=models.CharField(max_length=20)
     dailywages=models.CharField(max_length=20)
     description=models.CharField(max_length=200)
     category = models.CharField(max_length=50) 


class Complaints(models.Model):
     name=models.CharField(max_length=20)
     email=models.CharField(max_length=20)
     number=models.IntegerField()
     message=models.CharField(max_length=200)



class Feedback(models.Model):
     name=models.CharField(max_length=20)
     message=models.CharField(max_length=200)



class Gallery(models.Model):
     workername=models.CharField(max_length=20)
     desc=models.CharField(max_length=500)
     imgg=models.ImageField(upload_to='gallery/')


class  Workerbooking(models.Model):
    username = models.CharField(max_length=255)
    workername=models.CharField(max_length=255)
    date = models.DateField()
    requirement=models.TextField()
    w_status=models.CharField(max_length=30,choices=w_choice)