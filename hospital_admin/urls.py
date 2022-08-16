from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.admin_login, name='admin-login'),
    
    path('admin-dashboard/',
         views.admin_dashboard, name='admin-dashboard'),
    path('hospital-admin-profile/<int:pk>/', views.hospital_admin_profile,
         name='hospital-admin-profile'),

    path('appointment-list',views.appointment_list, name='appointment-list'),
    
    path('doctor-list/', views.doctor_list,name='doctor-list'),
    
    path('forgot-password/', views.admin_forgot_password,name='admin_forgot_password'),
    path('hospital-list/', views.hospital_list,name='hospital-list'),
    path('add-hospital/', views.add_hospital,name='add-hospital'),
    path('edit-hospital/<int:pk>/', views.edit_hospital,name='edit-hospital'),
    path('delete-hospital/<int:pk>/', views.delete_hospital,name='delete-hospital'),

    path('hospital-list/', views.hospital_list,name='hospital-list'),
    path('add-hospital/', views.add_hospital,name='add-hospital'),
    path('add-pharmacist/', views.add_pharmacist,name='add-pharmacist'),
    #path('edit-hospital/', views.edit_hospital,name='edit-hospital'),
    path('invoice/',views.invoice, name='invoice'),
    path('invoice-report/',views.invoice_report, name='invoice_report'),
    path('lock-screen/', views.lock_screen,name='lock_screen'),
    path('login/',views.admin_login,name='admin_login'),
    path('patient-list/',views.patient_list, name='patient-list'),
    # path('register/', views.register,name='register'),
    path('admin_register/',views.admin_register,name='admin_register'),
    path('transactions-list/',views.transactions_list, name='transactions_list'),
    path('admin-logout/', views.logoutAdmin, name='admin-logout'),

    path('emergency/', views.emergency_details,name='emergency'),
    path('edit-emergency-information/<int:pk>/', views.edit_emergency_information,name='edit-emergency-information'),
    
    path('hospital-profile/', views.hospital_profile ,name='hospital-profile'),
    path('hospital-admin-profile/<int:pk>/', views.hospital_admin_profile,
         name='hospital-admin-profile'),

   path('create-invoice/<int:pk>/', views.create_invoice,name='create-invoice'),

]  


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
