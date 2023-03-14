from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.buyer_register, name='register'),
    path('seller_register/', views.seller_register, name='seller_register'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('seller_dashboard/', views.seller_page, name='seller_page'),
    path('', views.dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/',
         views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),

]
