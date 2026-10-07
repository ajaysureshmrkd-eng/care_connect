from django.urls import path

from booking_v2.views import signUpView,AppointmentListCreateView,AppointmentRetrieveUpdateDeleteView

urlpatterns =[

    path("signup/",signUpView.as_view()),

    path('appointments/',AppointmentListCreateView.as_view()),
    path('appointments/<int:pk>/',AppointmentRetrieveUpdateDeleteView.as_view()),
    


]