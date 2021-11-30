from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [

    # path('signup/',views.signup_view,name='signup'),
    # path('login/',views.login_view,name='login'),
    # path('logout/',views.logout_view,name='logout'),

     path('',views.dashboard,name='dashboard'),
     path('register/',views.register,name='register'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     path('dashboard/',views.dashboard,name='dashboard'),
     path('activate/<uidb64>/<token>/',views.activate,name='activate'),
     path('forgotPassword/',views.forgotPassword, name='forgotPassword'),
     path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name='resetpassword_validate'),
     path('resetPassword/',views.resetPassword,name='resetPassword'),



]
