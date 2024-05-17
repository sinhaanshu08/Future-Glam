from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import FieldError
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import signin, Studentinfo, Appointment,Test


def Home(request):
    return render(request, 'Home.html')


def Login(request):
    return render(request, 'Login.html')


def Info(request):
    return render(request, 'Info.html')

def Profile1(request):
    return render(request, 'Profile1.html')

def Profile(request):
    email = request.session.get('user')
    print(email)
    student = Studentinfo.get_student_by_email(email)
    if student:
        return render(request, 'Profile.html', {'Studentinfo': student})
    else:
        return render(request, 'Profile1.html')


def Registration(request):
    email = request.session.get('user')
    print(email)
    student = signin(
        email=email,
    )
    if student.isExist():
        return render(request, 'Registration.html', {'student': student})


def Home2(request):
    return render(request, 'Home2.html')


def Contact(request):
    return render(request, 'Contact.html')


def Counselling(request):
    return render(request, 'Counselling.html')


def Test(request):
    return render(request, 'Test.html')


def Schedule(request):
    email = request.session.get('user')
    print(email)
    student = signin(
        email=email,
    )

    if student.isExist():
        return render(request, 'Schedule.html', {'student': student})


def Dash(request):
    return render(request, 'Dash.html')


def Exam(request):
    return render(request, 'Exam.html')


def Result(request):
    return render(request, 'Result.html')


def Eqtestresult(request):
    return render(request, 'Eqtestresult.html')

def Iitestresult(request):
    return render(request, 'Iitestresult.html')

def Iqtestresult(request):
    return render(request, 'Iqtestresult.html')

def Psycotestresult(request):
    return render(request, 'Psycotestresult.html')

def Selfconcepttestresult(request):
    return render(request, 'Selfconcepttestresult.html')

def Chat(request):
    return render(request, 'Chat.html')


def Thanks(request):
    return render(request, 'Thanks.html')

def Thanks1(request):
    return render(request, 'Thanks1.html')

def Thanks2(request):
    return render(request, 'Thanks2.html')

def Thanks3(request):
    return render(request, 'Thanks3.html')

def Thanks4(request):
    return render(request, 'Thanks4.html')


def Testinfo(request):
    return render(request, 'Testinfo.html')


def Rules(request):
    return render(request, 'Rules.html')


def Rules2(request):
    return render(request, 'Rules2.html')


def Rules3(request):
    return render(request, 'Rules3.html')


def Rules4(request):
    return render(request, 'Rules4.html')


def Rules5(request):
    return render(request, 'Rules5.html')


def Test_Appointment(request):
    email = request.POST.get('email')
    firstname = request.POST.get('fname')
    lastname = request.POST.get('lname')
    date = str(request.POST.get('date'))
    print(email, firstname, lastname, date)

    appoinment_info = Appointment(
        firstname=firstname,
        lastname=lastname,
        email=email,
        date=date
    )
    appoinment_info.register()
    return render(request, 'schedule.html',{'appoinment_info':appoinment_info})


def Signup(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email, password)
    student = signin(
        email=email,
        password=password
    )
    error_message = None
    request.session['user'] = student.email
    if student.isExist():
        if student.passwordmatch():
            return redirect('home2')

        else:
            error_message = 'Password incorrect'
            return render(request, 'Login.html', {'error': error_message})
    else:
        error_message = 'Email Incorrect Or Password Incorrect'
        return render(request, 'Login.html',{'error': error_message})



def Signin(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        print(email, username, password, password1)

        value = {
            'email': email,
            'username': username,
            'password': password
        }
        error_message = None

        student = signin(
            email=email,
            username=username,
            password=password
        )
        request.session['user'] = student.email
        if student.isExist():
            error_message = 'E-mail Address Already registered'
        if password != password1:
            error_message = 'Password and Confirm Password must be same'

        if not error_message:
            student.register()
            print(email, username, password, password1)
            request.session['signedemail'] = student.email
            return redirect('home2')
        else:
            error1= 'User Email ID already Exists'
            print(error1)
            return render(request, 'Login.html',{'error1' : error1} )

        # request.session['email'] = student.email


def Registration_new(request):
    # return render(request, "registration.html")
    # return HttpResponse('index page')
    if request.method == 'GET':
        return render(request, 'Profile.html')
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        saddress = request.POST.get('saddress')
        ssaddress = request.POST.get('ssaddress')
        city = request.POST.get('city')
        region = request.POST.get('region')
        xboard = request.POST.get('xboard')
        xiiboard = request.POST.get('xiiboard')
        guniversity = request.POST.get('guniversity')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        phone = request.POST.get('phone')
        zipcode = request.POST.get('zipcode')
        xyear = request.POST.get('xyear')
        xiiyear = request.POST.get('xiiyear')
        gyear = request.POST.get('gyear')
        parentsphone = request.POST.get('pphone')
        Xmarks = request.POST.get('Xmarks')
        Xiimarks = request.POST.get('Xiimarks')
        gmarks = request.POST.get('gmarks')
        date = request.POST.get('date')
        email = request.POST.get('email')
        parentsproff = request.POST.get('parentsproff')
        print(firstname, lastname, email, Xmarks)

        value = {
            'firstname': firstname,
            'lastname': lastname,
            'gender': gender,
            'saddress': saddress,
            'ssaddress': ssaddress,
            'city': city,
            'region': region,
            'xboard': xboard,
            'xiiboard': xiiboard,
            'guniversity': guniversity,
            'father': father,
            'mother': mother,
            'parentsproff': parentsproff,
            'phone': phone,
            'zipcode': zipcode,
            'xyear': xyear,
            'xiiyear': xiiyear,
            'gyear': gyear,
            'parentsphone': parentsphone,
            'Xmarks': Xmarks,
            'Xiimarks': Xiimarks,
            'gmarks': gmarks,
            'date': date,
            'email': email
        }

        error_message = None
        student = Studentinfo(
            firstname=firstname,
            lastname=lastname,
            gender=gender,
            saddress=saddress,
            ssaddress=ssaddress,
            city=city,
            region=region,
            xboard=xboard,
            xiiboard=xiiboard,
            guniversity=guniversity,
            father=father,
            mother=mother,
            parentsproff=parentsproff,
            phone=phone,
            zipcode=zipcode,
            xyear=xyear,
            xiiyear=xiiyear,
            gyear=gyear,
            parentsphone=parentsphone,
            Xmarks=Xmarks,
            Xiimarks=Xiimarks,
            gmarks=gmarks,
            date=date,
            email=email
        )
        if not firstname:
            error_message = 'First Name Required'
        elif not lastname:
            error_message = 'Last Name Required'
        elif not city:
            error_message = 'City/village Name Required'
        elif not xboard:
            error_message = '10hth Board Name Required'
        elif not xiiboard:
            error_message = '12th Board Name Required'
        elif not guniversity:
            error_message = 'Graduation university Name Required'
        elif not guniversity:
            error_message = 'Graduation university Name Required'
        elif not father:
            error_message = 'father Name Required'
        elif not mother:
            error_message = 'mother Name Required'
        elif not parentsproff:
            error_message = 'parentsproff  Required'
        elif not zipcode:
            error_message = 'Zipcode Required'
        elif not phone:
            error_message = 'Phone Required'
        elif len(phone) < 10:
            error_message = 'Phone Number Contain 10 Digits'
        elif not xyear:
            error_message = '10th Year Required'
        elif not xiiyear:
            error_message = '12th Year Required'
        elif not gyear:
            error_message = 'Graduation Year Required'
        elif not parentsphone:
            error_message = 'Gardians Phone Required'
        elif len(parentsphone) < 10:
            error_message = 'Phone Number Contain 10 Digits'
        elif not Xmarks:
            error_message = '10th Marks Required'
        elif not Xiimarks:
            error_message = '12th Marks Required'
        elif not gmarks:
            error_message = 'Graduation Marks Required'
        elif not date:
            error_message = 'Birth Date Required'
        elif not email:
            error_message = 'E-mail ID Required'

        if not error_message:
            student.register()
            return redirect('dash.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'home2.html', data)




def p6(request):
    return render(request, 'p6.html')


def p7(request):
    return render(request, 'p7.html')


def p8(request):
    return render(request, 'p8.html')


def p9(request):
    return render(request, 'p9.html')


def p10(request):
    return render(request, 'p10.html')


def I1(request):
    return render(request, 'I1.html')


def I2(request):
    return render(request, 'I2.html')


def I3(request):
    return render(request, 'I3.html')


def I4(request):
    return render(request, 'I4.html')


def I5(request):
    return render(request, 'I5.html')


def I6(request):
    return render(request, 'I6.html')


def I7(request):
    return render(request, 'I7.html')


def I8(request):
    return render(request, 'I8.html')


def I9(request):
    return render(request, 'I9.html')


def I10(request):
    return render(request, 'I10.html')


def a1(request):
    return render(request, 'a1.html')

def a2(request):
    return render(request, 'a2.html')

def a3(request):
    return render(request, 'a3.html')

def a4(request):
    return render(request, 'a4.html')

def a5(request):
    return render(request, 'a5.html')

def a6(request):
    return render(request, 'a6.html')

def a7(request):
    return render(request, 'a7.html')

def a8(request):
    return render(request, 'a8.html')

def a9(request):
    return render(request, 'a9.html')

def a10(request):
    return render(request, 'a10.html')

def a11(request):
    return render(request, 'a11.html')

def a12(request):
    return render(request, 'a12.html')

def a13(request):
    return render(request, 'a13.html')

def a14(request):
    return render(request, 'a14.html')

def a15(request):
    return render(request, 'a15.html')

def a16(request):
    return render(request, 'a16.html')

def a17(request):
    return render(request, 'a17.html')

def a18(request):
    return render(request, 'a18.html')

def a19(request):
    return render(request, 'a19.html')

def a20(request):
    return render(request, 'a20.html')

def a21(request):
    return render(request, 'a21.html')

def a22(request):
    return render(request, 'a22.html')

def a23(request):
    return render(request, 'a23.html')

def a24(request):
    return render(request, 'a24.html')

def a25(request):
    return render(request, 'a25.html')

def a26(request):
    return render(request, 'a26.html')

def a27(request):
    return render(request, 'a27.html')

def a28(request):
    return render(request, 'a28.html')

def a29(request):
    return render(request, 'a29.html')

def a30(request):
    return render(request, 'a30.html')

def a31(request):
    return render(request, 'a31.html')

def a32(request):
    return render(request, 'a32.html')

def a33(request):
    return render(request, 'a33.html')

def a34(request):
    return render(request, 'a34.html')

def a35(request):
    return render(request, 'a35.html')

def a36(request):
    return render(request, 'a36.html')

def a37(request):
    return render(request, 'a37.html')

def a38(request):
    return render(request, 'a38.html')

def a39(request):
    return render(request, 'a39.html')

def a40(request):
    return render(request, 'a40.html')

def a41(request):
    return render(request, 'a41.html')

def a42(request):
    return render(request, 'a42.html')

def a43(request):
    return render(request, 'a43.html')

def a44(request):
    return render(request, 'a44.html')

def a45(request):
    return render(request, 'a45.html')

def a46(request):
    return render(request, 'a46.html')

def a47(request):
    return render(request, 'a47.html')

def a48(request):
    return render(request, 'a48.html')

def a49(request):
    return render(request, 'a49.html')

def a50(request):
    return render(request, 'a50.html')

def a51(request):
    return render(request, 'a51.html')

def a52(request):
    return render(request, 'a52.html')

def E1(request):
    return render(request, 'E1.html')

def E2(request):
    return render(request, 'E2.html')

def E3(request):
    return render(request, 'E3.html')

def E4(request):
    return render(request, 'E4.html')

def E5(request):
    return render(request, 'E5.html')

def E6(request):
    return render(request, 'E6.html')

def E7(request):
    return render(request, 'E7.html')

def E8(request):
    return render(request, 'E8.html')

def E9(request):
    return render(request, 'E9.html')

def E10(request):
    return render(request, 'E10.html')

def S1(request):
    return render(request, 'S1.html')

def S2(request):
    return render(request, 'S2.html')

def S3(request):
    return render(request, 'S3.html')

def S4(request):
    return render(request, 'S4.html')

def S5(request):
    return render(request, 'S5.html')

def S6(request):
    return render(request, 'S6.html')

def S7(request):
    return render(request, 'S7.html')

def S8(request):
    return render(request, 'S8.html')

def S9(request):
    return render(request, 'S9.html')

def S10(request):
    return render(request, 'S10.html')