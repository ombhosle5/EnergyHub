from .views import userView,signupView,signinView,mainView,logoutView,energy_view,gas_view,power_view,sustainability_view,resources_view, contact_view,support_view
from django.urls import path

urlpatterns =[
    path("",userView,name='index'),
    path("signup/",signupView,name='signup'),
    path("signin/",signinView,name='signin'),
    path("main/",mainView,name='main'),
    path("logout/",logoutView,name='logout'),

    path('energy/', energy_view, name='energy'),
    path('gas/', gas_view, name='gas'),
    path('power/', power_view, name='power'),
    path('sustainability/', sustainability_view, name='sustainability'),
    path('resources/', resources_view, name='resources'),
    path('contact/', contact_view, name='contact'),
    path('support/', support_view, name='support'),

]