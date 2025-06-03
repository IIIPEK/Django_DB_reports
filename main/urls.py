from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.report_list, name='index'),
    path('report/add/', views.report_form_view, name='report_add'),
    path('report/<int:pk>/edit/', views.report_form_view, name='report_edit'),
    path('report/<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('alert/add/', views.alert_form_view, name='alert_add'),
    path('alert/<int:pk>/edit/', views.alert_form_view, name='alert_edit'),
    path('alert/<int:pk>/delete/', views.alert_delete, name='alert_delete'),
]