from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [

     # Basic Page For Everyone
     url(r'^$', views.index, name="Main Page"),
     path('myProfile', views.myProfile, name="myProfile Page"),

     # Change Profile For Patient & Medical
     path('changeProfile/<int:id>/', views.changeProfile, name="changeProfile Page"),
     
     # Update Profile For Patient & Medical
     path('updateProfile/<int:id>/', views.updateProfile, name="updateProfile Page"),

     # Change Pass
     path('changePass', views.changePass, name="Change Password"),

     # Login
     path('login', views.handleLogin, name="Login Page"),

     # Signup
     path('signup', views.signup, name="Signup Page"),

     # Logout
     path('logout', views.handleLogout, name="Logout Page"),

     # Pending Request For Create Account
     path('pendingRequest', views.pendingRequest, name="Pending Request"),

     # Accept Request For Create Account
     path('acceptProfile/<int:id>/', views.acceptProfile, name="Accept Request"),

     # Reject Request For Create Account
     path('rejectProfile/<int:id>/', views.rejectProfile, name="Reject Request"),

     # Admin Site
     path('adminSite', views.adminSite, name="Admin Site"),

     # All Users
     path('allUser', views.allUser, name="All User"),

     # Delete User
     path('delUser/<int:id>', views.delUser, name="Delete User"),

     # Admin Doctors List
     path('admin_doctors', views.admin_doctors, name="admin doctors"),
     
     # Admin Patient List
     path('admin_patients', views.admin_patients, name="admin patients"),
     
     # Admin Hospital List
     path('admin_hospital', views.admin_hospital, name="admin hospital"),
     
     # Admin Medical List
     path('admin_medical', views.admin_medical, name="admin medical"),
     
     # Admin Reports List
     path('admin_reports', views.admin_reports, name="admin hospital"),

     # Admin Patient Search
     path('admin_patients_search', views.admin_patients_search, name="admin patients search"),

     # Search Query in Admin Panel
     path('searchQuery', views.searchQuery, name="admin patients search"),

     # Search Doctor for Patient    
     path('searchDoctor_patient', views.searchDoctor_patient, name="search doctor"),

     # Doctor Profile
     path('doctor_profile', views.doctor_profile, name="Doctor Profile"),
     
     # Doctor Change Profile
     path('doctorChangeProfile/<int:id>/', views.doctorChangeProfile, name="Doctor Update Profile Page"),
     
     # Doctor Update Profile
     path('doctorUpdateProfile/<int:id>/', views.doctorUpdateProfile, name="Doctor Update Profile Page"),

     # Doctor Change Password
     path('doctorChangePass', views.doctorChangePass, name="Change Password"),

     # Doctor Book Appoinment
     path('bookAppoinment/<int:pId>/<int:dId>/', views.bookAppoinment, name="Book Appoinment"),
     
     # View All Appoinments
     path('doctor_appoinments/<int:id>/', views.doctor_appoinments, name="Appoinments"),
     
     # Doctor's Patients
     path('doctor_myPatients/<int:id>/', views.doctor_myPatients, name="Appoinments"),

     # Doctor Accept Appoimment
     path('acceptAppoinment/<int:docId>', views.acceptAppoinment, name="Appoinments"),
     
     # Doctor Reject Appoinment
     path('deniedAppoinment/<int:docId>/', views.deniedAppoinment, name="Appoinments"),

     # Handle Payment By Paytm Payment Gateway
     path('handlePayment', views.handlePayment, name="Handle Payment"),

     # Pending Appoinment For Patient
     path('pending_appoinment', views.pending_appoinment, name="Pending Appoinment"),

     # Complate Appoinment For Patient
     path('complate_appoinment', views.complate_appoinment, name="Complate Appoinment"),

     # History Of all Appoinment For Patient
     path('history_appoinment', views.history_appoinment, name="History Appoinment"),

     # Doctor Patient Dashboard
     path('doctor_patient_dashboard/<int:pId>/<int:appoId>/', views.doctor_patient_dashboard, name="Doctor Patient Dashboard"),

     # Add Prescription Page For Doctor
     path('addPrescriptions/<int:id>/<int:uId>',views.addPrescriptions, name="Add Prescriptions"),
    
     # View Prescription for All
     path('viewPrescription/<int:id>/',views.viewPrescription, name="View Prescriptions"),
     
     # Add Medical Report For Doctor
     path('addMedicalRecords/<int:pId>/<int:appoId>/', views.addMedicalRecords, name="Add Medical Records"),

     # Create Bill
     path('createBill/<int:pId>/<int:appoId>/', views.createBill, name="Create Bill"),
    
     # View Bill For All
     path('viewBill/<int:id>/', views.viewBill, name="View Bill"),

     # Doctor All Invoice
     path('doctor_invoice/', views.doctor_invoice , name="Doctor Invoice"),
    
     # Patient View Invoice
     path('invoice/', views.invoice , name="All Invoice"),
     
     # Search Patient For Medical
     path('searchPatientMedical/', views.searchPatientMedical , name="Search Medical Patient"),
     
     # Verify Account
     path('verify-account/<str:uid>', views.verifyAccount , name="Search Medical Patient"),

     # Add Patient By Doctor
     path('add-patient-by-doctor', views.addPatientByDoctor , name="Add Patient By Doctor"),

     path('authenticate-username', views.validateUsername , name="Add Patient By Doctor"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
