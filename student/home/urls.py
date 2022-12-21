from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.Home.as_view(),name='home'),
    path('staff/',views.Staffs.as_view(),name='staff'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('student/',views.Student.as_view(),name='student'),
    path('editprofile/',views.Editprofile.as_view(),name='editprofile'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('form/',views.Form.as_view(),name='form'),
    path('edit/',views.Edit.as_view(),name='edit'),
    path('delete/',views.Delete.as_view(),name='delelte'),

]

