from django.urls import path ,include

from accounts.views import signupView
urlpatterns = [
    path("",include("django.contrib.auth.urls")),
    path ("signup" ,signupView.as_view() , name="signup" )
]