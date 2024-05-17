from django.db import models

# Create your models here.
class signin(models.Model):
    email = models.CharField(max_length=50, default='', null=False)
    username = models.CharField(max_length=50, default='', null=False)
    password = models.CharField(max_length=50, default='', null=False)

    def register(self):
        self.save()

    def get_user_by_email(email):
        try:
            return signin.objects.get(email=email)
        except:
            return False

    def isExist(self):

        if signin.objects.filter(email=self.email):
            return True
        else:
            return False
    def passwordmatch(self):

        if signin.objects.filter(password=self.password):
            return True
        else:
            return False

class Studentinfo(models.Model):
    firstname = models.CharField(max_length=50, default='', null=False)
    lastname = models.CharField(max_length=50, default='', null=False)
    gender = models.CharField(max_length=20, default='', null=False)
    saddress = models.CharField(max_length=50, default='', null=False)
    ssaddress = models.CharField(max_length=50, default='', null=False)
    city = models.CharField(max_length=50, default='', null=False)
    region = models.CharField(max_length=50, default='', null=False)
    xboard = models.CharField(max_length=100, default='', null=False)
    xiiboard = models.CharField(max_length=100, default='', null=False)
    guniversity = models.CharField(max_length=100, default='', null=False)
    father = models.CharField(max_length=100, default='', null=False)
    mother = models.CharField(max_length=50, default='', null=False)
    parentsproff = models.CharField(max_length=50, default='', null=False)
    phone = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    xyear = models.IntegerField(default=0)
    xiiyear = models.IntegerField(default=0)
    gyear = models.IntegerField(default=0)
    parentsphone = models.IntegerField(default=0)
    Xmarks = models.FloatField(default=0)
    Xiimarks = models.FloatField(default=0)
    gmarks = models.FloatField(default=0)
    date = models.DateField()
    email = models.EmailField()

    def register(self):
        self.save()


    @staticmethod
    def get_all_student():
        return Studentinfo.objects.all()

    @staticmethod
    def get_studentinfo_by_name(email):
        return Studentinfo.objects.filter(email=email)

    @staticmethod
    def get_student_by_email(email):
        try:
            return Studentinfo.objects.get(email=email)
        except:
            return False

    #def isExist(self):

       # if Studentinfo.objects.filter(email=self.email):
       #     return True
        #else:
        #    return False


class Result(models.Model):
    total_score = models.IntegerField(default=0)
    test_type = models.CharField(max_length=50, default='', null=False)
    test_name = models.CharField(max_length=50, default='', null=False)





class Appointment(models.Model):
    firstname = models.CharField(max_length=50, default='', null=False)
    lastname = models.CharField(max_length=50, default='', null=False)
    email = models.CharField(max_length=50, default='', null=False)
    date = models.CharField(max_length=50, default='', null=False)

    def register(self):
        self.save()

    @staticmethod
    def get_schedule_by_email(email):
        try:
            return Appointment.objects.filter(email=email)
        except:
            return

class Test(models.Model):
    tname = models.CharField(max_length=50, default='', null=False)
    ttype = models.CharField(max_length=50, default='', null=False)
    question = models.CharField(max_length=50, default='', null=False)
    answer = models.CharField(max_length=50, default='', null=False)
    option1 = models.CharField(max_length=50, default='', null=False)
    option2 = models.CharField(max_length=50, default='', null=False)
    option3 = models.CharField(max_length=50, default='', null=False)

    def register(self):
        self.save()