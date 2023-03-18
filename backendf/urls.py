from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admeme/',views.getadmin),
    path('',views.getlog),
    path('doc/',views.getdocs),
    path('docx',views.getdocx),
    path('appoint',views.getappo),
    path('register/',registerviewset.as_view({'post':'setlog'})),
    path('meeting/',meetingviewset.as_view({'post':'meeting'})),
    path('update/',updatepass.as_view({'post':'update'})),
    path('addservice/',updateservice.as_view({'post':'addservice'})),
    path('adddoc/',addDoctorviewset.as_view({'post':'adddoc'})),
    path('deldoc/',removeDoctorviewset.as_view({'post':'deldoc'})),
    path('delmeet/',deletes.as_view({'post':'delslot'})),
    path('delcate/',delcateview.as_view({'post':'delcategory'})),
    path('updoc/',updaterepviewset.as_view({'post':'updaterepo'}))
]
