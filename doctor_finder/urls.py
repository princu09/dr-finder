from django.contrib import admin
from django.urls import path, include
from doctor import urls

admin.site.site_header = "Dr.Finder By NFG"
admin.site.index_title = "Welcome to Dr.Finder NFG"

urlpatterns = [
    path('siteAdminApproveByNFG/', admin.site.urls),
    path('', include('doctor.urls')),
]