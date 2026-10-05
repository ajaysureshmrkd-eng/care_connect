from django.urls import path

from booking_v2.views import signUpView

urlpatterns =[

    path("signup/",signUpView.as_view()),
    


]