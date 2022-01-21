from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path('data-chart/', views.data_chart, name='data-chart'),
   path('grade-chart/', views.grade_chart, name='grade-chart'),
   path("goals/", views.goals, name="goals"),
   path("account/", views.account, name="account"),
]