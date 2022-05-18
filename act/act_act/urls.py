from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('', views.WorksList.as_view(), name='work_list'),
    path('<int:pk>/', views.WorksDetail.as_view(), name='work_detail')
])