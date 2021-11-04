# Page Redirect , Request Page , Response Page
import json
from django.shortcuts import render, HttpResponse, redirect
# Showing Message alert on Main Page
from django.contrib import messages
# Create account
from django.contrib.auth.models import User, auth
# import Tables
from doctor.models import CustomUser, BookAppoinment, Prescriptions, MedicalReports, Bill
# Login account
from django.contrib.auth import authenticate, login, logout
# Change Password
from django.contrib.auth.forms import PasswordChangeForm
# Gmail Request Add
from django.core.mail import send_mail
# Import json
from django.http import JsonResponse
# For Search Query
from django.db.models import Q
# Store User Image
from django.core.files.storage import FileSystemStorage
# CSRF Token
from django.views.decorators.csrf import csrf_exempt , csrf_protect
# Paytm Gateway
from PayTm import Checksum
# Date Time
from django.utils.timezone import datetime
from datetime import date
import uuid
from django.conf import settings

# Merchant Key For Paytm
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'


def index(request):
    drData = CustomUser.objects.filter(fieldName="Doctor")
    return render(request, 'index.html', context={'drData': drData})


def myProfile(request):
    if request.method == "POST":
        billNo = request.POST['billNo']
        billData = Bill.objects.filter(id=billNo)
        context = {'billData': billData}
    userData = BookAppoinment.objects.filter(patientId=request.user.id)
    appo = Prescriptions.objects.filter(patientId=request.user.id)
    mediReport = MedicalReports.objects.filter(patientId=request.user.id)
    bill = Bill.objects.filter(patientId=request.user.id)
    context = {'userData': userData, 'appo': appo,
               'mediReport': mediReport, 'bill': bill}
    return render(request, 'myProfile.html', context)


def changeProfile(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'changeProfile.html', {"editData": user})


def updateProfile(request, id):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        blood = request.POST['blood']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        dob = request.POST['dob']

        try:
            userImg = request.FILES['userImg']
            fs = FileSystemStorage()
            filename = fs.save(userImg.name, userImg)
            uploaded_file_url = fs.url(filename)
            user = CustomUser.objects.filter(id=id).update(userImg=userImg)
        except:
            pass

        user = CustomUser.objects.filter(id=id).update(
            first_name=fname, last_name=lname, mobile=mobile, email=email, bloodGroup=blood, address=address, city=city, state=state, dob=dob)
    return redirect('/myProfile')


def changePass(request):
    if request.method == 'POST':
        oPass = request.POST['oPass']
        nPass = request.POST['nPass']
        cPass = request.POST['cPass']

        if (oPass == "") or (nPass == "") or (cPass == "") or (nPass != cPass):
            messages.error(
                request, "Please Check Password and Enter All Fields")
            return redirect('/changePass')
        else:
            if (len(nPass) >= 5):
                if (oPass == nPass):
                    messages.error(request, "Please Enter Valid New Password")
                    return redirect('/changePass')
                else:
                    user = CustomUser.objects.get(id=request.user.id)
                    check = user.check_password(oPass)
                    if check == True:
                        user.set_password(nPass)
                        user.save()
                        messages.success(
                            request, "Your Password Change Successfully !")
                        return redirect('/')
            else:
                messages.error(
                    request, "Please Enter Password More than 5 Char.")
                return redirect('/changePass')
    return render(request, 'user/changePass.html')


def handleLogin(request):
    if request.method == 'POST':
        loginUsername = request.POST['usrname']
        loginPassword = request.POST['password']

        if loginUsername == "admin":
            user = authenticate(username=loginUsername, password=loginPassword)
            if user is not None:
                login(request, user)
                return redirect('/adminSite')

        else:
            user = authenticate(username=loginUsername, password=loginPassword)
            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        post = request.POST['checkBtn']
        fname = request.POST['fname']
        lname = request.POST['lname']
        usrName = request.POST['usrname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['pass']
        status = "pending"
        uid = uuid.uuid4()

        checkQuery2 = CustomUser.objects.filter(mobile=mobile).exists()
        if checkQuery2 == True:
            CustomUser.objects.filter(mobile=mobile).update(username=usrName, first_name=fname, last_name=lname, email=email, fieldName=post, status=status, amount=0, token=uid , createdByUser=True)
            a = CustomUser.objects.get(mobile=mobile)
            a.set_password(password)
            a.save()

                
            user = authenticate(username=usrName, password=password)
            if user is not None:
                login(request, user)
                send_mail('Dr.Finder Account Verification Mail', f'This is verification email , please verify your account using the link http://127.0.0.1:8000/verify-account/{uid}', 'pmkvyprince@gmail.com', [email], fail_silently=False)
                return redirect('/')                

        else:
            u = CustomUser.objects.create_user(username=usrName, first_name=fname, last_name=lname,email=email, password=str(password), fieldName=post,mobile=mobile, status=status, amount=0, token=uid,createdByUser=True)
            u.save()

            user = authenticate(username=usrName, password=password)
            if user is not None:
                login(request, user)

                send_mail('Dr.Finder Account Verification Mail', f'This is verification email , please verify your account using the link http://127.0.0.1:8000/verify-account/{uid}', 'pmkvyprince@gmail.com', [email], fail_silently=False)
                return redirect('/')       

    return render(request, 'signup.html')


def handleLogout(request):
    logout(request)
    return redirect('/')


def pendingRequest(request):
    getUserData = CustomUser.objects.filter(status="pending")
    context = {'userData': getUserData}
    return render(request, 'adminSite/pendingRequest.html', context)


def acceptProfile(request, id):
    if request.method == "POST":
        user = CustomUser.objects.filter(id=id).update(status="success")
    return redirect('/pendingRequest')


def rejectProfile(request, id):
    if request.method == "POST":
        uid = request.POST['userId']
        u = CustomUser.objects.get(id=id)
        u.delete()
    return redirect('/pendingRequest')


def adminSite(request):
    print(request.user)
    getUserData = CustomUser.objects.all()
    getDoctor = CustomUser.objects.filter(fieldName="Doctor").count()
    getPatients = CustomUser.objects.filter(fieldName="Patient").count()
    getHospital = CustomUser.objects.filter(fieldName="Hospital").count()
    getMedical = CustomUser.objects.filter(fieldName="Medical").count()
    context = {'userData': getUserData, 'getDoctor': getDoctor,
               'getPatients': getPatients, 'getHospital': getHospital, 'getMedical': getMedical}
    return render(request, 'adminSite/index.html', context)


def allUser(request):
    getUserData = CustomUser.objects.all()
    context = {'userData': getUserData}
    return render(request, 'adminSite/allUser.html', context)


def delUser(request, id):
    if request.method == "POST":
        user = CustomUser.objects.get(id=id)
        user.delete()
    return redirect('/allUser')


def admin_doctors(request):
    getUserData = CustomUser.objects.filter(fieldName="Doctor")
    context = {'userData': getUserData}
    return render(request, 'adminSite/admin_doctors.html', context)


def admin_patients(request):
    getUserData = CustomUser.objects.filter(fieldName="Patient")
    context = {'userData': getUserData}
    return render(request, 'adminSite/admin_patients.html', context)


def admin_hospital(request):
    getUserData = CustomUser.objects.filter(fieldName="Hospital")
    context = {'userData': getUserData}
    return render(request, 'adminSite/admin_hospital.html', context)


def admin_medical(request):
    getUserData = CustomUser.objects.filter(fieldName="Medical")
    context = {'userData': getUserData}
    return render(request, 'adminSite/admin_medical.html', context)


def admin_reports(request):
    getUserData = MedicalReports.objects.all()
    context = {'userData': getUserData}
    return render(request, 'adminSite/admin_reports.html', context)


def admin_patients_search(request):
    if request.is_ajax():
        mobile = request.GET.get('mobile')

        getUserData = CustomUser.objects.get(mobile=mobile)
        # User Data
        fName = getUserData.first_name
        lName = getUserData.last_name
        last_login = getUserData.last_login
        mobile = getUserData.mobile
        email = getUserData.email
        dob = getUserData.dob
        bloodGroup = getUserData.bloodGroup
        address = getUserData.address
        city = getUserData.city
        state = getUserData.state
        status = getUserData.status
        date_joined = getUserData.date_joined
        staff = getUserData.is_staff
        superUser = getUserData.is_superuser

        return JsonResponse({
            'fName': fName,
            'lName': lName,
            'last_login': last_login,
            'dob': dob,
            'mobile': mobile,
            'email': email,
            'bloodGroup': bloodGroup,
            'address': address,
            'city': city,
            'state': state,
            'status': status,
            'date_joined': date_joined,
            'staff': staff,
            'superUser': superUser,
        }, status=200)
    return render(request, 'adminSite/search_patients.html')


def searchQuery(request):
    if request.method == "POST":
        query = request.POST['q']
        if query != "":
            doctorQ = CustomUser.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(username__contains=query) | Q(email__contains=query) | Q(
                mobile__contains=query) | Q(dob__contains=query) | Q(bloodGroup__contains=query) | Q(address__contains=query) | Q(city__contains=query) | Q(state__contains=query)).filter(fieldName="Doctor")
            dcQ = len(doctorQ)

            patientsQ = CustomUser.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(username__contains=query) | Q(email__contains=query) | Q(
                mobile__contains=query) | Q(dob__contains=query) | Q(bloodGroup__contains=query) | Q(address__contains=query) | Q(city__contains=query) | Q(state__contains=query)).filter(fieldName="Patient")
            ptQ = len(patientsQ)

            hospitalQ = CustomUser.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(username__contains=query) | Q(email__contains=query) | Q(
                mobile__contains=query) | Q(dob__contains=query) | Q(bloodGroup__contains=query) | Q(address__contains=query) | Q(city__contains=query) | Q(state__contains=query)).filter(fieldName="Hospital")

            hpQ = len(hospitalQ)

            medicalQ = CustomUser.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query) | Q(username__contains=query) | Q(email__contains=query) | Q(
                mobile__contains=query) | Q(dob__contains=query) | Q(bloodGroup__contains=query) | Q(address__contains=query) | Q(city__contains=query) | Q(state__contains=query)).filter(fieldName="Medical")

            mediQ = len(medicalQ)

            context = {'query': query, 'doctorQ': doctorQ, 'dcQ': dcQ,
                       'patientsQ': patientsQ, 'ptQ': ptQ, 'hospitalQ': hospitalQ, 'hpQ': hpQ, 'mediQ': mediQ, 'medicalQ': medicalQ}

            return render(request, 'adminSite/search.html', context)
        else:
            return redirect('/adminSite')
    return redirect('adminSite')


def searchDoctor_patient(request):
    if request.method == "POST":
        name = request.POST['name']
        location = request.POST['location']
        gender = request.POST['gender']
        spDr = request.POST['spDr']
        print(gender)

        if name != "" and location != "" and gender != "":
            qs = CustomUser.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name) | Q(city__contains=location) | Q(
                state__contains=location)).filter(gender=gender).filter(fieldName="Doctor")
            context = {'queryset': qs}
            return render(request, 'searchDoctor_patient.html', context)

        else:
            if name != "" and location != "":
                print("1")
                qs = CustomUser.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name) | Q(
                    city__contains=location) | Q(state__contains=location)).filter(fieldName="Doctor")
                context = {'queryset': qs}
                return render(request, 'searchDoctor_patient.html', context)

            if location != "" and gender != "Choose...":
                qs = CustomUser.objects.filter(Q(city__contains=location) | Q(
                    state__contains=location)).filter(gender=gender).filter(fieldName="Doctor")
                context = {'queryset': qs}
                return render(request, 'searchDoctor_patient.html', context)

        if name != "":
            qs = CustomUser.objects.filter(
                Q(first_name__contains=name) | Q(last_name__contains=name)).filter(fieldName="Doctor")
            context = {'queryset': qs}
            return render(request, 'searchDoctor_patient.html', context)

        if location != "":
            qs = CustomUser.objects.filter(Q(city__contains=location) | Q(
                state__contains=location)).filter(fieldName="Doctor")
            context = {'queryset': qs}
            return render(request, 'searchDoctor_patient.html', context)

        if gender != "":
            qs = CustomUser.objects.filter(
                gender=gender).filter(fieldName="Doctor")
            context = {'queryset': qs}
            return render(request, 'searchDoctor_patient.html', context)

    return render(request, 'searchDoctor_patient.html')


def doctor_profile(request):
    today = date.today()
    currentUser = request.user.id
    bookAppo = BookAppoinment.objects.filter(
        doctorId=currentUser).filter(approve=True)

    pendingAppo = BookAppoinment.objects.filter(doctorId=currentUser).filter(
        approve=True).filter(complateAppoinment=False)

    todayAppo = BookAppoinment.objects.filter(doctorId=currentUser).filter(
        approve=True).filter(complateAppoinment=False).filter(date=today)

    upcomingAppo = BookAppoinment.objects.filter(doctorId=currentUser).filter(
        approve=True).filter(complateAppoinment=False).exclude(date=today)

    complateAppo = BookAppoinment.objects.filter(
        doctorId=currentUser).filter(approve=True, complateAppoinment=True)

    try:
        delAppo = BookAppoinment.objects.filter(doctorId=currentUser).filter(
            approve=True).filter(complateAppoinment=False)

        if delAppo[0].date < today:
            u = delAppo[0]
            u.delete()
    except:
        pass

    context = {'bookAppo': bookAppo, 'pendingAppo': pendingAppo,
               'todayAppo': todayAppo, 'upcomingAppo': upcomingAppo, 'complateAppo': complateAppo}
    return render(request, 'doctor/doctor_myProfile.html', context)


def doctorChangeProfile(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'doctor/doctor_change_profile.html', {"editData": user})


def doctorUpdateProfile(request, id):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        blood = request.POST['blood']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        dob = request.POST['dob']
        amount = request.POST['amount']
        try:
            userImg = request.FILES['userImg']
            fs = FileSystemStorage()
            filename = fs.save(userImg.name, userImg)
            uploaded_file_url = fs.url(filename)
            user = CustomUser.objects.filter(id=id).update(userImg=userImg)
        except:
            pass

        user = CustomUser.objects.filter(id=id).update(first_name=fname, last_name=lname, mobile=mobile,
                                                       email=email, bloodGroup=blood, address=address, city=city, state=state, dob=dob, amount=amount)

    return redirect('/doctor_profile')


def doctorChangePass(request):
    if request.method == 'POST':
        oPass = request.POST['oPass']
        nPass = request.POST['nPass']
        cPass = request.POST['cPass']

        if (oPass == "") or (nPass == "") or (cPass == "") or (nPass != cPass):
            messages.error(
                request, "Please Check Password and Enter All Fields")
            return redirect('/changePass')
        else:
            if (len(nPass) >= 5):
                if (oPass == nPass):
                    messages.error(request, "Please Enter Valid New Password")
                    return redirect('/changePass')
                else:
                    user = CustomUser.objects.get(id=request.user.id)
                    check = user.check_password(oPass)
                    if check == True:
                        user.set_password(nPass)
                        user.save()
                        messages.success(
                            request, "Your Password Change Successfully !")
                        return redirect('/')
            else:
                messages.error(
                    request, "Please Enter Password More than 5 Char.")
                return redirect('/changePass')
    return render(request, 'doctor/doctor_change_password.html')


def bookAppoinment(request, pId, dId):
    if request.user.fieldName == "Doctor":
        return redirect('/')
    doctorDetails = CustomUser.objects.filter(
        id=dId).filter(fieldName="Doctor")

    patientDetails = CustomUser.objects.filter(
        id=pId).filter(fieldName="Patient")

    context = {'d': doctorDetails, 'p': patientDetails}

    if request.method == "POST":
        name = request.user.first_name + " " + request.user.last_name
        date = request.POST['date']
        amount = doctorDetails[0].amount

        b = BookAppoinment(date=date, payment=False, doctorId=dId, patientName=name,
                           approve=False, time="00:00:00", complateAppoinment=False, amount=amount, patientId=pId)

        b.save()

        amount = doctorDetails[0].amount
        email = doctorDetails[0].email

        orderId = BookAppoinment.objects.last()
        orderId2 = orderId.bookId

        # Request For payment
        parameters_dict = {
            'MID': 'WorldP64425807474247',
            'ORDER_ID': str(orderId2),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlePayment',
        }

        parameters_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
            parameters_dict, MERCHANT_KEY)

        return render(request, 'user/paymentDoctor.html', {'parameters_dict': parameters_dict})
    return render(request, 'user/bookAppoinment.html', context)


def doctor_appoinments(request, id):
    h = BookAppoinment.objects.filter(approve=False).filter(doctorId=id)
    context = {'h': h}
    return render(request, 'doctor/doctor_appoinments.html', context)


def doctor_myPatients(request, id):
    bookData = BookAppoinment.objects.filter(doctorId=id).filter(complateAppoinment=True)
    userId = []
    for i in bookData:
        a = CustomUser.objects.get(id=i.patientId)
        userId.append(a)
    return render(request, 'doctor/doctor_patients.html' , context={'userId':userId})


def acceptAppoinment(request, docId):
    if request.method == "POST":
        id = request.POST['bookIdPut']
        time = request.POST['time']
        h = BookAppoinment.objects.filter(bookId=id)
        h.update(approve=True, time=time)
        return redirect(f'/doctor_appoinments/{docId}')


def deniedAppoinment(request, docId):
    if request.method == "POST":
        getId = request.POST['bookIdPut2']
        h = BookAppoinment.objects.filter(bookId=getId)
        h.delete()
        return redirect(f'/doctor_appoinments/{docId}')


@csrf_exempt
def handlePayment(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)

    if verify:
        if response_dict['RESPCODE'] == '01':
            paymentStatus = response_dict['ORDERID']
            u = BookAppoinment.objects.filter(
                bookId=paymentStatus).update(payment=True)
            u.save()
    return render(request, 'user/paymentstatus.html', {'response': response_dict})


def pending_appoinment(request):
    currentUser = request.user.id
    pendingAppo = BookAppoinment.objects.filter(
        patientId=currentUser).filter(complateAppoinment=False)

    doctorID = []
    for i in pendingAppo:
        doctorID.append(i.doctorId)

    doctorName = []
    for j in doctorID:
        dName = CustomUser.objects.filter(id=j)
        fname = dName[0].first_name
        lname = dName[0].last_name
        name = f"{fname} {lname}"
        doctorName.append(name)

    myList = zip(pendingAppo, doctorName)
    return render(request, 'user/pending_appoinment.html', context={'myList': myList})


def complate_appoinment(request):
    currentUser = request.user.id
    complateAppo = BookAppoinment.objects.filter(
        patientId=currentUser).filter(complateAppoinment=True)

    doctorID = []
    for i in complateAppo:
        doctorID.append(i.doctorId)

    doctorName = []
    for j in doctorID:
        dName = CustomUser.objects.filter(id=j)
        fname = dName[0].first_name
        lname = dName[0].last_name
        name = f"{fname} {lname}"
        doctorName.append(name)

    myList = zip(complateAppo, doctorName)
    return render(request, 'user/complate_appoinment.html', context={'myList': myList})


def history_appoinment(request):
    currentUser = request.user.id
    historyAppo = BookAppoinment.objects.filter(patientId=currentUser)

    doctorID = []
    for i in historyAppo:
        doctorID.append(i.doctorId)

    doctorName = []
    for j in doctorID:
        dName = CustomUser.objects.filter(id=j)
        fname = dName[0].first_name
        lname = dName[0].last_name
        name = f"{fname} {lname}"
        doctorName.append(name)

    myList = zip(historyAppo, doctorName)
    return render(request, 'user/history_appoinment.html', context={'myList': myList})


def doctor_patient_dashboard(request, pId, appoId):
    userData = CustomUser.objects.filter(id=pId)

    appo = BookAppoinment.objects.filter(bookId=appoId)

    prescriptions = Prescriptions.objects.filter(appoId=appoId)

    mediReport = MedicalReports.objects.filter(
        appoId=appoId).filter(patientId=pId)

    bill = Bill.objects.filter(patientId=pId)

    context = {'userData': userData, 'appo': appo, 'pId': pId,
               'prescriptions': prescriptions, 'appoId': appoId, 'mediReport': mediReport, 'bill': bill}

    return render(request, 'doctor/doctor_patient_dashboard.html', context)


def addPrescriptions(request, id, uId):
    if request.method == "POST":
        name = request.POST.getlist('tblName')
        qty = request.POST.getlist('tblQty')
        days = request.POST.getlist('tblDays')
        tblTime = request.POST.getlist('tblTime')

        if Prescriptions.objects.filter(appoId=id).exists():
            data = Prescriptions.objects.filter(appoId=id)

            n = data[0].tblName
            for i in range(len(name)):
                n.append(name[i])

            q = data[0].qty
            for i in range(len(qty)):
                q.append(qty[i])

            d = data[0].days
            for i in range(len(days)):
                d.append(days[i])

            t = data[0].tblTime
            for i in range(len(tblTime)):
                t.append(tblTime[i])

            data.update(tblName=n, qty=q, days=d, tblTime=t)
            return redirect(f'/doctor_patient_dashboard/{uId}/{id}')
        else:
            u = Prescriptions.objects.create(
                appoId=id, tblName=name, qty=qty, days=days, tblTime=tblTime, patientId=uId)
            u.save()
            return redirect(f'/doctor_patient_dashboard/{uId}/{id}')

    getData = BookAppoinment.objects.filter(bookId=id)
    context = {'getData': getData}
    return render(request, 'doctor/add_prescription.html', context)


def viewPrescription(request, id):
    userData = Prescriptions.objects.filter(appoId=id)

    dataName = []
    for i in range(len(userData[0].tblName)):
        dataName.append(userData[0].tblName[i])

    dataQty = []
    for i in range(len(userData[0].tblName)):
        dataQty.append(userData[0].qty[i])

    dataDays = []
    for i in range(len(userData[0].tblName)):
        dataDays.append(userData[0].days[i])

    tblTime = []
    for i in range(len(userData[0].tblName)):
        tblTime.append(userData[0].tblTime[i])

    myList = zip(dataName, dataQty, dataDays, tblTime)

    context = {'userData': userData, 'myList': myList}
    return render(request, 'doctor/view_prescription.html', context)


def addMedicalRecords(request, pId, appoId):
    if request.method == "POST" and request.FILES['report']:
        date = request.POST['date']
        desc = request.POST['desc']
        report = request.FILES['report']
        fs = FileSystemStorage(location="media/reports")
        filename = fs.save(report.name, report)
        uploaded_file_url = fs.url(filename)

        m = MedicalReports.objects.create(
            appoId=appoId, patientId=pId, date=date, desc=desc, report=report)
        m.save()

    return redirect(f'/doctor_patient_dashboard/{pId}/{appoId}')


def createBill(request, pId, appoId):
    if request.method == "POST":
        date = request.POST['date']
        billName = request.POST.getlist('billName')
        bill = request.POST.getlist('bill')

        sum = 0
        for i in range(len(bill)):
            sum = sum + int(bill[i])

        patientData = CustomUser.objects.filter(id=pId)
        name = patientData[0].first_name + " " + patientData[0].last_name
        docId = request.user.id
        docName = request.user.first_name + " " + request.user.last_name

        createBill = Bill.objects.create(patientId=pId, patientName=name, doctorId=docId, doctorName=docName,
                                         date=date, itemName=billName, itemBill=bill, totalBill=sum, appoId=appoId)
        createBill.save()

        BookAppoinment.objects.filter(
            bookId=appoId).update(complateAppoinment=True)

        return redirect(f'/doctor_patient_dashboard/{pId}/{appoId}')


def viewBill(request, id):
    billData = Bill.objects.filter(id=id)

    iName = []
    for i in range(len(billData[0].itemName)):
        iName.append(billData[0].itemName[i])

    iItem = []
    for i in range(len(billData[0].itemBill)):
        iItem.append(billData[0].itemBill[i])

    myList = zip(iName, iItem)

    return render(request, 'doctor/view_Bill.html', context={'billData': billData, 'myList': myList})


def doctor_invoice(request):
    billData = Bill.objects.filter(doctorId=request.user.id)
    return render(request, 'doctor/doctor_invoice.html', context={'billData': billData})


def invoice(request):
    bill = Bill.objects.filter(patientId=request.user.id)
    return render(request, 'invoice.html', context={'bill': bill})


def searchPatientMedical(request):
    return render(request, 'searchPatientMedical.html')


def verifyAccount(request, uid):
    CustomUser.objects.filter(token=uid).update(status="success")
    return redirect('/')


def addPatientByDoctor(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        usrname = uuid.uuid4()

        checkQuery = CustomUser.objects.filter(mobile=mobile).exists()
        if checkQuery == True:
            pass
        else:
            u = CustomUser.objects.create(username=usrname, first_name=fname, last_name=lname,
                                          fieldName="Patient", status="pending", mobile=mobile, amount=0)
            u.save()

        uId = CustomUser.objects.get(mobile=mobile)
        uId = uId.id

        dId = request.user.id
        amount = request.user.amount

        name = fname + " " + lname
        time = datetime.now().strftime('%H:%M:%S')

        b = BookAppoinment.objects.create(date=date.today(), payment=True, doctorId=dId, patientName=name,
                                          approve=True, time=time, complateAppoinment=True, patientId=uId, amount=amount)

        bId = BookAppoinment.objects.filter(doctorId=dId).last()
        bId = bId.bookId
        return redirect(f'/doctor_patient_dashboard/{uId}/{bId}')

@csrf_exempt
def validateUsername(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({"username_error" : "Sorry Username is already exists."}, status=409)
        return JsonResponse({"username_valid" : True})