from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('create_order', create_order, name='create_order'),
    path('certification', vendor_list_view, name='certifications'),
    path('certification/<slug:v_id>', vendor_exam_list_view, name='exams'),
    path('certification/<slug:v_id>/<slug:e_id>', exam_question_list_view, name='questions'),
    path('admin_tools', admin_tools, name='admin_tools'),
]